
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_chrome_driver(headless=False):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    if headless:
        chrome_options.add_argument("--headless=new")  # New headless mode for newer Chrome
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

    service = Service('chromedriver.exe')  # Assuming chromedriver.exe is in the same folder
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver