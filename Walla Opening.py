import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Install ChromeDriver and configure options
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open walla web
    driver.get("http://www.walla.co.il")
    driver.maximize_window()  # Optional: Maximize the browser window
    wait = WebDriverWait(driver, 30)

finally:
    # Close the browser
    driver.quit()