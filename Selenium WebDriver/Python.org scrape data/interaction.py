from selenium import webdriver
from selenium.webdriver.common.by import By

WIKI_URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome()
driver.get(WIKI_URL)
total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
print(total_articles)