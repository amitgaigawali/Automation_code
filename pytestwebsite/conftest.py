from selenium import webdriver
from time import sleep
import pytest


# @pytest.fixture(scope='module')
# from pytestfunctions import arithmetic_class
# from pytestfunctions.arithmetic_class import ArithmeticClass


@pytest.fixture(scope='class')
def OneTimeSetUp(request):
    print('setting driver path')
    driver = webdriver.Chrome(executable_path="C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")
    # screenshot_path = "C:\\Users\\amitg\\PycharmProjects\\screenshot\\"
    sleep(4)
    driver.maximize_window()

    print('launching Browser')
    driver.get("https://www.google.com/")
    request.cls.driver = driver
    yield driver
    print('driver close')
    driver.close()
    print('driver quit')
    driver.quit()

# @pytest.fixture(scope='module')
# def SetUp():
#     ac = arithmetic_class.ArithmeticClass()
