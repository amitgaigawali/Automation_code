from selenium import webdriver
from time import time
import pytest

@pytest.fixture()
def SetUp():
    driver = webdriver.Chrome(executable_path = "C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")
    screenshot_path = "C:\\Users\\amitg\\PycharmProjects\\screenshot\\"
    yield
    driver.close()


def test_browser_launch(SetUp):
    # print("setting driver path ")
    # print("launching browser")
    SetUp.driver.get("https://www.goindigo.in/")

    assert True
    SetUp.driver.save_screenshot(SetUp.screenshot_path +str(round(time()))+".png")
    # print('driver close')
@pytest.mark.last
def test_homepage_title(SetUp):
    # print("getting homepage title ")
    # print('comparing title')
    title =SetUp.driver.title

    assert title =='indigo'
    # print('driver close')

def test_browser_link(SetUp):
    # print("getting all links ")
    # print('validating links from homepage')
    search_flight = SetUp.driver.find_element_by_xpath("//span[text()='Search Flight']")
    search_flight.click()
    SetUp.driver.save_screenshot(SetUp.screenshot_path +str(round(time())+".png")
    # print('driver close')