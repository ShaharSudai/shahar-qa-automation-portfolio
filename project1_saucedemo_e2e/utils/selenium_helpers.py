from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

DEFAULT_TIMEOUT = 10

def init_driver() -> WebDriver:
    # Start a Chrome WebDriver instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def quit_driver(driver: WebDriver) -> None:
    # Close the WebDriver instance
    driver.quit()

def parse_locator(locator_str: str):
    strategy, value = locator_str.split("=", 1)
    s = strategy.strip().lower()
    if s == "id":
        return By.ID, value
    if s == "name":
        return By.NAME, value
    if s == "css":
        return By.CSS_SELECTOR, value
    if s == "xpath":
        return By.XPATH, value
    if s == "class":
        return By.CLASS_NAME, value
    raise ValueError(f"Unknown locator strategy: {strategy}")

def wait_and_click(driver: WebDriver, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    element.click()
    return element

def enter_text(driver: WebDriver, by: By, locator: str, text: str, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    element.clear()
    element.send_keys(text)
    return element

def get_text(driver: WebDriver, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    return element.text.strip()

def get_attribute(driver, by, locator, name, timeout=DEFAULT_TIMEOUT):
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    return element.get_attribute(name)

def click_and_switch_to_new_tab(driver, by, locator, timeout=10):
    original = driver.current_window_handle
    existing = set(driver.window_handles)
    el = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    el.click()
    WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > len(existing))
    new_handle = [h for h in driver.window_handles if h not in existing][0]
    driver.switch_to.window(new_handle)
    return original

def close_tab_and_switch_back(driver, original_handle):
    driver.close()
    driver.switch_to.window(original_handle)