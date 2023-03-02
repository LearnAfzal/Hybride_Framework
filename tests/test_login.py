import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginUI:

    """@pytest.fixture(scope="function",autouse=True)
    def configure"""
    def test_title(self): # we no need to create object eplicitly, pytest library will take care of creating object thats why we are makins use of "test" as prefix
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(25)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title=driver.title
        assert actual_title == "OrangeHRM"
        assert 'HRM' in actual_title # to find the availability of partial text in title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(25)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_header=driver.find_element(By.XPATH,"//h5").text
        assert_that("Login").is_equal_to(actual_header)


