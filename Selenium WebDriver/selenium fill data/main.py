from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

URL = 'http://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.find_element(By.XPATH, value='/html/body/form/input[1]').send_keys('Dima')
driver.find_element(By.XPATH, value='/html/body/form/input[2]').send_keys('Balaka')
driver.find_element(By.XPATH, value='/html/body/form/input[3]').send_keys('dsada@dsada.com')
driver.find_element(By.CLASS_NAME, value='btn-primary').click()

