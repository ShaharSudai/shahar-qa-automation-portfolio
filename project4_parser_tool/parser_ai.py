from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json, ast, re

from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def compute_xpath(el):
    path=[]
    node=el
    while getattr(node,"name",None) and node.name!="[document]":
        idx=len(list(node.find_previous_siblings(node.name)))+1
        path.append(f"{node.name}[{idx}]")
        node=node.parent
    path.reverse()
    return "/"+"/".join(path)

def extract_elements(html: str):
    soup=BeautifulSoup(html,"html.parser")
    elements=[]
    for el in soup.find_all(True):
        try:
            elements.append({
                "tag":el.name,
                "id":el.get("id"),
                "class":el.get("class"),
                "name":el.get("name"),
                "type":el.get("type"),
                "placeholder":el.get("placeholder"),
                "aria_label":el.get("aria-label"),
                "data_testid":el.get("data-testid"),
                "text":el.get_text(strip=True)[:120],
                "xpath":compute_xpath(el)
            })
        except Exception:
            continue
    return elements

def strip_code_fences(text: str) -> str:
    return re.sub(r"^```(?:python)?\s*|\s*```$","",text.strip(),flags=re.IGNORECASE|re.DOTALL)

def ask_model(elements, task: str):
    llm=ChatOllama(model="qwen2.5-coder",temperature=0)
    prompt=ChatPromptTemplate.from_template(
        """You receive a JSON array of page elements with fields: tag, id, class, name, type, placeholder, aria_label, data_testid, text, xpath.
{elements}

Task: {task}

Return Python code only. Output a valid Python module that defines a single top-level dict named CONFIG.
Rules:
- CONFIG keys: semantic snake_case names (e.g., username_field, password_field, login_button, search_input).
- CONFIG values: a single locator string using exactly one of:
  - id=VALUE
  - class=VALUE
  - xpath=VALUE
- Prefer stable unique locators: id first, then a single class if unique, otherwise xpath.
- No explanations or markdown. Importable code only.
"""
    )
    chain=prompt|llm|StrOutputParser()
    text_elements=json.dumps(elements,ensure_ascii=False)
    return chain.invoke({"elements":text_elements,"task":task})

def save_python_module(code: str, filename: str="config.py"):
    cleaned=strip_code_fences(code)
    ast.parse(cleaned)
    with open(filename,"w",encoding="utf-8") as f:
        f.write(cleaned)

def pick_page(pages, filter_text: str):
    cand=pages
    if filter_text:
        ft=filter_text.lower()
        cand=[pg for pg in pages if ft in (pg.url or "").lower() or ft in (pg.title() or "").lower()]
        if not cand:
            cand=pages
    print("\nOpen tabs:")
    for i,pg in enumerate(cand):
        try:
            title=pg.title()
        except Exception:
            title=""
        print(f"[{i}] {pg.url}  |  {title}")
    choice=input("Pick tab index (Enter for 0): ").strip()
    idx=int(choice) if choice.isdigit() and 0<=int(choice)<len(cand) else 0
    return cand[idx]

def grab_selected_tab_html(debug_url="http://127.0.0.1:9222"):
    with sync_playwright() as p:
        browser=p.chromium.connect_over_cdp(debug_url)
        all_pages=[]
        for ctx in browser.contexts:
            all_pages.extend([pg for pg in ctx.pages if pg.url and not pg.url.startswith("chrome")])
        if not all_pages:
            browser.close()
            raise RuntimeError("No tabs found")
        filt=input("Filter (URL/title contains, Enter to skip): ").strip()
        page=pick_page(all_pages,filt)
        page.wait_for_load_state("domcontentloaded")
        html=page.content()
        browser.close()
        return html

if __name__=="__main__":
    html=grab_selected_tab_html("http://127.0.0.1:9222")
    elements=extract_elements(html)
    task = input("Now which elements you want me to find? ") + " and produce CONFIG as specified"
    print("I'm on it, just wait a few seconds...")
    code=ask_model(elements,task)
    save_python_module(code,"config.py")
    print("config.py file has been saved")
