import sys, json
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

print("Working on it...")
def get_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()
    return html

def build_css_selector(el):
    _id = el.get("id")
    if _id:
        return f"#{_id}"
    cls = el.get("class", [])
    cls_sel = ''.join(f".{c}" for c in cls)
    return f"{el.name}{cls_sel}" if cls_sel else el.name

def build_xpath(el):
    parts = []
    cur = el
    while cur and getattr(cur, "name", None):
        if cur.parent:
            siblings = [sib for sib in cur.parent.find_all(cur.name, recursive=False)]
            idx = siblings.index(cur) + 1
            parts.append(f"{cur.name}[{idx}]")
        else:
            parts.append(cur.name)
        cur = cur.parent
    return "/" + "/".join(reversed(parts))

def parse(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    elements = []
    for el in soup.find_all(True):
        rec = {
            "tag": el.name,
            "id": el.get("id"),
            "name": el.get("name"),
            "type": el.get("type"),
            "classes": el.get("class", []),
            "placeholder": el.get("placeholder"),
            "text": el.get_text(strip=True) if el.get_text() else "",
            "css": build_css_selector(el),
            "xpath": build_xpath(el),
        }
        elements.append(rec)
    return {
        "source_url": url,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "elements": elements
    }

if __name__ == "__main__":
    url = sys.argv[1]
    data = parse(url)
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(data['elements'])} elements to output.json")
