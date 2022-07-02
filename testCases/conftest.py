from selenium import webdriver
import pytest

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/")
    request.cls.driver = driver

    yield driver
    driver.close()