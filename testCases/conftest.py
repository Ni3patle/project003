from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome" :
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.....")
    elif browser == "firefox" :
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        print("Launching Firefox Browser.....")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.....")
    return  driver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############################# html report ############################

def pytest_configure(config):
    config._metadata['Project Name']= 'Nop Commerce'
    config._metadata['Module Name']= 'Customers'
    config._metadata['tester']='Nitin S.Patle'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


