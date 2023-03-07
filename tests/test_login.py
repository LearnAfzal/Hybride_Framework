import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper

class TestLoginUI(WebDriverWrapper):

    # even if we dont mention scope option also it will take "function" as default because its only scope which works inside class
    # autouse=true -> to make use of this configure_webbrowser inside all non-static test methods or otherwise we need to individually mention the method name in test emthod-arguments like (self, configure_webbrowser)

    def test_title(self): # we no need to create object eplicitly, pytest library will take care of creating object thats why we are makins use of "test" as prefix
        actual_title=self.driver.title
        assert actual_title == "OrangeHRM"
        assert 'HRM' in actual_title # to find the availability of partial text in title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header=self.driver.find_element(By.XPATH,"//h5").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholders(self):
        actual_username_placeholder=self.driver.find_element(By.NAME, "username").get_attribute("placeholder")
        actual_password_placeholder=self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        print("Valid login")
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        actual_header = self.driver.find_element(By.XPATH, "//h6").text
        assert_that("Dashboard").is_equal_to(actual_header)

    @pytest.mark.parametrize("username,password,expected_error",[
        ("john","john123","Invalid credentials"),
        ("jack","jack123","Invalid credentials")
    ])
    def test_invalid_login(self,username,password,expected_error):
        print("InValid login")
        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").text
        assert_that(expected_error).is_equal_to(actual_error)