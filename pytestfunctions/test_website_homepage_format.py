import pytest



@pytest.fixture()
def SetUp():
    print('setting driver path')
    print('launching Browser')
    yield
    print('driver close')

def test_browser_launch(SetUp):
    assert True

def test_homepage_title():
    print('getting homepage title')
    print('comparing title')
    assert True

def test_homepage_link(SetUp):
    print('getting all links')
    print('validating links from homepage')
    assert False
