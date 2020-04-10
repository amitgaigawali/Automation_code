import pytest
from pytestfunctions import conftest
from conftest import OneTimeSetUp




@pytest.fixture()
def SetUp():
    print('setting driver path')
    print('launching Browser')
    yield
    print('driver close')

def test_browser_launch(OneTimeSetUp):
    assert True

def test_homepage_title(OneTimeSetUp):
    print('getting homepage title')
    print('comparing title')
    assert True

def test_homepage_link(OneTimeSetUp):
    print('getting all links')
    print('validating links from homepage')
    assert False
