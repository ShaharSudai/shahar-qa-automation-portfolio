import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()
