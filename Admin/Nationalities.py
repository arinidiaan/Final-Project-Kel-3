import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
fake = Faker()

class TestNationalities(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_nationalities(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Nationalities']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)
        
unittest.main()