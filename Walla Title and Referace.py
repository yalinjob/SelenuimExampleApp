import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Install ChromeDriver and configure options
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()

# Initialize WebDriver
try:
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Step 1: Open Walla website
    url = "http://www.walla.co.il"
    driver.get(url)

    # Wait until the page title is accessible
    wait = WebDriverWait(driver, 30)
    initial_title = driver.title  # Get the title of the website
    print(f"Initial title: {initial_title}")

    # Step 2: Refresh the website
    driver.refresh()

    # Step 3: Get the website title after refresh and compare
    refreshed_title = driver.title  # Get the title again
    print(f"Refreshed title: {refreshed_title}")

    # Compare the titles
    if initial_title == refreshed_title:
        print("The website titles are the same after refresh!")
    else:
        print("The website titles are different after refresh!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Closing the browser...")
    driver.quit()
