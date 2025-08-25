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

def wait_and_click(driver: WebDriver, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
    # Wait until the element is clickable and click it
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
    element.click()
    return element

def enter_text(driver: WebDriver, by: By, locator: str, text: str, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
    # Wait until the element is visible and type text into it
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    element.clear()
    element.send_keys(text)
    return element

def get_text(driver: WebDriver, by: By, locator: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    #Wait until the element is visible and return its text
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    return element.text.strip()
