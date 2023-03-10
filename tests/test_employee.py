import pytest
import time
from selenium import webdriver
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,firstname,middlename,lastname,actual_header,actual_first_name",data_source.test_add_valid_employee_data)
    def test_add_valid_employee(self,username,password,firstname,middlename,lastname,actual_header,actual_first_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_name = self.driver.find_element(By.XPATH, f"//h6[contains(normalize-space(),'{firstname}')]").text #to handle dynammic xpath based on firstname
        assert_that(actual_header).is_equal_to(actual_name)
        #time.sleep(5)
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.NAME, "firstName"), "value", firstname))
        actual_fname = self.driver.find_element(By.NAME, "firstName").get_attribute("value") # this value attribute is not visible in inspect element but for all the input fields it will be there(hidden element)
        assert_that(actual_first_name).is_equal_to(actual_fname)

    @pytest.mark.parametrize("username,password,upload_filepath,error_msg",data_source.test_invalid_profile_upload_data)
    def test_invalid_profile_upload(self, username, password, upload_filepath, error_msg):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@type='file']").send_keys(upload_filepath)
        actual_error=self.driver.find_element(By.XPATH,"//span[text()='File type not allowed']").text
        assert_that(error_msg).is_equal_to(actual_error)
        time.sleep(5)
        print(actual_error)