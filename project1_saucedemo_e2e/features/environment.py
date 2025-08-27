import sys
from pathlib import Path
from selenium import webdriver

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding")
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")

    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()
