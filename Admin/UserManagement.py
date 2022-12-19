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

class TestUserManagement(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_login(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        time.sleep(5)

        response__data = browser.find_element(By.XPATH, "(//*[text()= 'Dashboard'])[1]").text

        self.assertEqual(response__data, 'Dashboard')

    def test_admin(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text()= 'Admin']").click()
        time.sleep(5)

    def test_search_by_usermanager(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Username'])[1]/parent::*/following-sibling::*/child::*").send_keys("Admin")
        browser.find_element(By.XPATH, "//*[text()= ' Search ']").click()
        time.sleep(5)
    
    def test_seacrh_by_userole(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "((//*[text() = 'User Role'])[1]/parent::*/following-sibling::*/child::*/child::*/child::*)[2]").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Admin'])[3]").click()
        browser.find_element(By.XPATH, "//*[text()= ' Search ']").click()
        time.sleep(3)

    def test_seacrh_by_employe_name(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Employee Name'])[1]/parent::*/following-sibling::*/child::*/child::*/child::input").send_keys("Alice")
        browser.find_element(By.XPATH, "//*[text()= 'Alice  Duval']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Search ']").click()
        time.sleep(5)

    def test_seacrh_by_status(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "((//*[text()= 'Status'])[1]/parent::*/following-sibling::*/child::*/child::*/child::*)[2]").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Enabled'])[1]").click()
        browser.find_element(By.XPATH, "//*[text()= ' Search ']").click()
        time.sleep(5)

    def test_seacrh_by_invalid_username(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Username'])[1]/parent::*/following-sibling::*/child::*").send_keys("hasvysa")
        browser.find_element(By.XPATH, "//*[text()= ' Search ']").click()
        time.sleep(5)

unittest.main()