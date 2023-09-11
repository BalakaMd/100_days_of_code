from selenium import webdriver
from selenium.webdriver.common.by import By

KSP_URL = 'https://ksp.co.il/cart/'
URL = 'https://ksp.co.il/cart/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# price = driver.find_element(By.CLASS_NAME, value='jss182')
# print(price.text)



