from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitter:

    def __init__(self, username, password):
        option = webdriver.ChromeOptions()
        option.add_argument("--incognito")
        self.driver = webdriver.Chrome("chromedriver.exe", options=option)
        self.name = username
        self.passw = password

    def begin(self):
        self.driver.get('https://twitter.com/login')

    def login(self):
        self.begin()
        time.sleep(2)
        self.__login(self.name, self.passw)
        time.sleep(2)
        try:
            y = self.driver.find_element_by_xpath(
                '//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]').text
            if y == "The username and password you entered did not match our records. Please double-check and try again." or y == "The email and password you entered did not match our records. Please double-check and try again.":
                self.driver.quit()
                return False
            elif y == "There was unusual login activity on your account. To help keep your account safe, please enter your phone number or username to verify it’s you.":
                self.driver.quit()
                return False
        except:
            pass
        self.__get_user()
        return True

    def __login(self, user, passwo):
        username = self.driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        username.send_keys(user)
        password = self.driver.find_element_by_xpath('//input[@name="session[password]"]')
        password.send_keys(passwo)
        password.send_keys(Keys.RETURN)

    def __get_user(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/a').click()
        self.url = self.driver.current_url
        time.sleep(2)
        self.__scrape()

    def __scrape(self):
        self.username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span[1]/span').text
        self.followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[2]/a/span[1]/span').text
        self.following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/a/span[1]/span').text
        try:
            self.tweet = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div').text
        except:
            self.tweet = "No Recent Tweets Found"
        self.driver.quit()
