from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach', True)

twitter_url = 'https://twitter.com/i/flow/signup'
speed_test_url = 'https://www.speedtest.net/ru'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrom_options)
        self.max_download = 0
        self.max_upload = 0

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        start_test_path = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        start_test = self.driver.find_element(By.CLASS_NAME, value='start-button')
        start_test.click()
        time.sleep(60)
        self.max_download = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.max_upload = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
        print(self.max_download)
        print(self.max_upload)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
