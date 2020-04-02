from selenium import webdriver
import pytest

def test_url_open_chrome():
    driver = webdriver.Chrome(executable_path ="C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()

def test_url_open_firefox():
    driver = webdriver.Firefox(executable_path="C:\\Users\\amitg\\PycharmProjects\\webdriver\\geckodriver.exe")
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    # driver.implicitly_wait(2)
    driver.close()


# test_url_open_chrome()
# test_url_open_firefox()