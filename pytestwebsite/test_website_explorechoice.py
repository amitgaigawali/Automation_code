from selenium import webdriver
import pytest
import time


# to use conftest.py file from package we have to set @pytest.mark.usefuxture("function_name01", "functions_name02", ....)

@pytest.mark.usefixtures("setUp", "take_screenshot")
class TestWebsiteHome:

    # when we are using one function for many test_cases then we have to set @pytest.fixture() to the "called function"
    @pytest.fixture()
    def classSetUp(self, autouse=True):
        print('This is class level setup can be used to initialize objects used in this class')
        current_window = self.driver.current_window_handle
        print(current_window)
        size = self.driver.get_window_size(current_window)
        print(size)
    #to use fixture function we have to pass that function name as parameter
    def test_homepage_title(self, classSetUp):
        page_title = self.driver.title
        assert page_title == 'explorechoice.org'

    def test_course_title(self, classSetUp):
        banner = self.driver.find_element_by_class_name("lead")
        banner_text = banner.text
        assert banner_text == "let's explore in & out of programming...."

    def test_testimonial_title(self, classSetUp):
        banner = self.driver.find_element_by_class_name("lead")
        banner_text = banner.text
        print(banner_text)

## What if we have multiple test case and is it necessary to pass at once - please refer
# test_website_two.py
