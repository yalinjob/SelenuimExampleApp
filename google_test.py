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
    # Step 1: Open Google Translate
    driver.get("https://translate.google.com")
    driver.maximize_window()  # Optional: Maximize the browser window

    # Step 2: Wait for the text area to become visible
    wait = WebDriverWait(driver, 10)
    input_text_area = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Source text"]'))
    )

    # Step 3: Write Hebrew text into the input field
    hebrew_text = "שלום, איך אתה?"
    input_text_area.send_keys(hebrew_text)

    # Step 4: Validate the text entered (Optional)
    entered_text = input_text_area.get_attribute("value")
    assert entered_text == hebrew_text, f"Expected: {hebrew_text}, but got: {entered_text}"
    print("Hebrew text entered successfully!")

finally:
    # Close the browser
    driver.quit()


