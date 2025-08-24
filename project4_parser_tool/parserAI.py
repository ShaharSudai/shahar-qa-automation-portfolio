from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json, ast, re
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_html(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()
        return html

def compute_xpath(el):
    path = []
    node = el
    while getattr(node, "name", None) and node.name != "[document]":
        same_tag_prev = len(list(node.find_previous_siblings(node.name)))
        index = same_tag_prev + 1
        path.append(f"{node.name}[{index}]")
        node = node.parent
    path.reverse()
    return "/" + "/".join(path)

def extract_elements(html: str):
    soup = BeautifulSoup(html, "html.parser")
    elements = []
    for el in soup.find_all(True):
        try:
            elements.append({
                "tag": el.name,
                "id": el.get("id"),
                "class": el.get("class"),
                "name": el.get("name"),
                "type": el.get("type"),
                "placeholder": el.get("placeholder"),
                "aria_label": el.get("aria-label"),
                "data_testid": el.get("data-testid"),
                "text": el.get_text(strip=True)[:80],
                "xpath": compute_xpath(el)
            })
        except Exception:
            continue
    return elements

def strip_code_fences(text: str) -> str:
    return re.sub(r"^```(?:python)?\s*|\s*```$", "", text.strip(), flags=re.IGNORECASE | re.DOTALL)

def ask_model(elements, task: str):
    llm = ChatOllama(model="qwen2.5-coder", temperature=0)
    prompt = ChatPromptTemplate.from_template(
        """You receive a JSON array of page elements with fields: tag, id, class, name, type, placeholder, aria_label, data_testid, text, xpath.
{elements}

Task: {task}

Return Python code only. Output a valid Python module that defines a single top-level dict named CONFIG.
Rules:
- CONFIG keys: semantic snake_case names (e.g., username_field, password_field, login_button).
- CONFIG values: a single locator string using exactly one of:
  - id=VALUE
  - class=VALUE
  - xpath=VALUE
- Prefer stable unique locators: id first, then a single class if unique, otherwise xpath.
- Do not include explanations or markdown. Output must be importable.
"""
    )
    chain = prompt | llm | StrOutputParser()
    text_elements = json.dumps(elements, ensure_ascii=False)
    return chain.invoke({"elements": text_elements, "task": task})

def save_python_module(code: str, filename: str = "config.py"):
    cleaned = strip_code_fences(code)
    ast.parse(cleaned)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(cleaned)

if __name__ == "__main__":
    url = input("Provide me the site URL please: ")
    html = get_html(url)
    elements = extract_elements(html)
    #"Select login-related elements and produce CONFIG as specified"
    task = input("Thanks, Now which elements you want me to find? ") + " and produce CONFIG as specified"
    print("I'm on it, just wait a few seconds...")
    code = ask_model(elements, task)
    save_python_module(code, "config.py")
    print("config.py file has been saved, go check it out!")
