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

class TestQualifications(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_qualification_by_skill(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Qualifications ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Skills']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= 'Description']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)

    def test_qualification_by_education(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Qualifications ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Education']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Level']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)

    def test_qualification_by_licenses(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Qualifications ']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Licenses'])[1]").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()

    def test_qualification_by_languages(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Qualifications ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Languages']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)    

    def test_qualification_by_memberships(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Qualifications ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Memberships']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)


unittest.main()
