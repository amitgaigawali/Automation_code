from selenium import webdriver
import pytest


# A - Arrange (set up/ prerequisite)
# A - Action (execution)
# A - Assertion/validation
def test_url_open_chrome():
    driver = webdriver.Chrome(executable_path="C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    paage_title = driver.title
    assert paage_title == 'indigo'

    # if(paage_title == 'indigo'):
    #   print('its matching')
    # else:
    #   print('its not matching')


def test_url_open_firefox():
    driver = webdriver.Firefox(executable_path="C:\\Users\\amitg\\PycharmProjects\\webdriver\\geckodriver.exe")
    driver.get("https://www.goindigo.in/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    paage_title = driver.title

    assert paage_title == 'indigo'

    driver.close()


    # if (paage_title == 'indigo'):
    #   print('its matching')
    # else:
    #   print('its not matching')

# test_url_open_chrome()
# test_url_open_firefox()
