import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)
driver.get('file:////Users/yalina/Downloads/tip_calc/index.html')
driver.find_element(By.XPATH, '//*[@id="billamt"]').send_keys(100)
driver.find_element(By.XPATH, '//*[@id="serviceQual"]/option[5]').click()
driver.find_element(By.XPATH, '//*[@id="peopleamt"]').send_keys(4)
driver.find_element(By.XPATH, '//*[@id="calculate"]').click()

result = driver.find_element(By.XPATH, '//*[@id="tip"]').text
assert result == '2.50', f"The value is: {result}"