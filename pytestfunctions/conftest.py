import pytest


@pytest.fixture(scope='module')
def OneTimeSetUp():
    print('setting driver path')
    print('launching Browser')
    yield
    print('driver close')
