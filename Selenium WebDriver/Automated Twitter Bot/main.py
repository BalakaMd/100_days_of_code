from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option('detach', True)
chrom_options.add_argument("--lang=en")

twitter_url = 'https://twitter.com/i/flow/login'
speed_test_url = 'https://www.speedtest.net/ru'
twitter_email = 'phyton.test.acc@gmail.com'
twitter_password = '7CAsTF$qn3-W?dU'
twitter_username = "TestPhyton"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrom_options)
        self.max_download = 0
        self.max_upload = 0

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        start_test = self.driver.find_element(By.CLASS_NAME, value='start-button')
        start_test.click()
        time.sleep(50)
        self.max_download = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.max_upload = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
        print(self.max_download)
        print(self.max_upload)

    def tweet_at_provider(self):
        self.driver.get(twitter_url)
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH, value="//input[@autocomplete='username']")
        email_input.send_keys(twitter_email)
        email_input.send_keys(Keys.ENTER)

        time.sleep(2)
        username_input = self.driver.find_element(By.TAG_NAME, value='input')
        username_input.send_keys(twitter_username)
        username_input.send_keys(Keys.ENTER)
        time.sleep(1)
        password_input = self.driver.find_elements(By.TAG_NAME, value='input')
        password_input[1].send_keys(twitter_password)
        password_input[1].send_keys(Keys.ENTER)
        time.sleep(3)
        twit = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                        'div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
                                                        'div[2]/div[1]/div/div/div/div/div/div/div/div/div/'
                                                        'div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        twit.click()
        twit.send_keys(f"My Current Internet Speed is {self.max_download} Download and {self.max_upload} Upload")
        send_twit = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                             'div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                             'div[2]/div[2]/div/div/div[2]/div[3]')
        send_twit.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
