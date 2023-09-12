from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

URL = 'https://www.python.org/'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_list = [event.text.split("\n") for event in events.find_elements(By.CSS_SELECTOR, value='li')]

events_dict = {}
for event in events_list:
    for n in range(len(events_list)):
        events_dict[n] = {'date': event[0],
                          'Event': event[1]}

print(events_dict)


driver.quit()
