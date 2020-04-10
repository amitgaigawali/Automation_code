from selenium import webdriver
from time import time, sleep
import pytest


@pytest.mark.usefixtures("OneTimeSetUp")
class TestMyWebsite:

    # @pytest.fixture()
    # def SetUp(self):
    #     self.driver = webdriver.Chrome(executable_path="C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")
    #     screenshot_path = "C:\\Users\\amitg\\PycharmProjects\\screenshot\\"
    #     sleep(4)
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.google.com/")
    #     yield self.driver
    #     self.driver.close()

    def test_website_launch(self):
        # print("setting driver path ")
        # print("launching browser")
        screenshot_path = "C:\\Users\\amitg\\PycharmProjects\\screenshot\\"
        Displayed = self.driver.find_element_by_xpath("//div/a[text()='Gmail']").is_displayed()
        title_website = self.driver.title
        file_name = str(round(time()))
        self.driver.save_screenshot(screenshot_path +file_name  +".png ")
        print(title_website)
        assert True == Displayed

    def test_homepage_title(self):
        # print("getting homepage title ")
        # print('comparing title')
        title = self.driver.title
        print(title)
        assert title == 'Google'

    def test_browser_link(self):
        # print("getting all links ")
        # print('validating links from homepage')
        links = self.driver.find_elements_by_tag_name('a')
        print(links)
        # search_mail = self.driver.find_element_by_xpath("//div/a[text()='Gmail']")
        # search_mail.click()
        file_name = str(round(time()))
        self.driver.save_screenshot("file_name+.png")
        assert 0 < len(links)
