from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

game_url = 'https://orteil.dashnet.org/experiments/cookie/'

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrom_options)
driver.get(game_url)
cookie = driver.find_element(By.ID, value='cookie')

timer = t.time() + 5


def bue_upgrade():
    money = int(driver.find_element(By.ID, value='money').text.replace(',', ''))
    if money > 123456789:
        time_machine = driver.find_element(By.ID, value='buyTime machine')
        time_machine.click()
    elif money > 1000000:
        portal = driver.find_element(By.ID, value='buyPortal')
        portal.click()
    elif money > 50000:
        shipment = driver.find_element(By.ID, value='buyShipment')
        shipment.click()
    elif money > 2000:
        mine = driver.find_element(By.ID, value='buyMine')
        mine.click()
    elif money >= 500:
        factory = driver.find_element(By.ID, value='buyFactory')
        factory.click()
    elif money >= 100:
        grandma = driver.find_element(By.ID, value='buyGrandma')
        grandma.click()
    else:
        cursor = driver.find_element(By.ID, value='buyCursor')
        cursor.click()


while True:
    if t.time() > timer:
        bue_upgrade()
        timer = t.time() + 15
    cookie.click()
