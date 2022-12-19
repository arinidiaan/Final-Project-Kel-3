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

class TestOrganization(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_organization_by_general_information(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()='Organization ']").click()
        browser.find_element(By.XPATH, "//*[text()='General Information']").click()
        browser.find_element(By.XPATH, "//*[text()='Edit']/child::span").click()
        browser.find_element(By.XPATH, "//*[text()='Organization Name']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()='Organization Name']/parent::*/following-sibling::*/child::*").send_keys(" Edit")
        browser.find_element(By.XPATH, "//*[text()= 'Registration Number']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Registration Number']/parent::*/following-sibling::*/child::*").send_keys("12345678")
        browser.find_element(By.XPATH, "//*[text()= 'Tax ID']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Tax ID']/parent::*/following-sibling::*/child::*").send_keys("11223344")
        browser.find_element(By.XPATH, "//*[text()= 'Phone']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Phone']/parent::*/following-sibling::*/child::*").send_keys("088888882828")
        browser.find_element(By.XPATH, "//*[text()= 'Fax']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Fax']/parent::*/following-sibling::*/child::*").send_keys("098765")
        browser.find_element(By.XPATH, "//*[text()= 'Email']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Email']/parent::*/following-sibling::*/child::*").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.XPATH, "//*[text()= 'Email']/parent::*/following-sibling::*/child::*").send_keys(Keys.DELETE)
        browser.find_element(By.XPATH, "//*[text()= 'Email']/parent::*/following-sibling::*/child::*").send_keys("a@example.com")
        browser.find_element(By.XPATH, "//*[text()= 'Address Street 1']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Address Street 1']/parent::*/following-sibling::*/child::*").send_keys("JL.Indonesia.raya")
        browser.find_element(By.XPATH, "//*[text()= 'City']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'City']/parent::*/following-sibling::*/child::*").send_keys("Indonesia")
        browser.find_element(By.XPATH, "//*[text()= 'State/Province']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'State/Province']/parent::*/following-sibling::*/child::*").send_keys("Java Place")
        browser.find_element(By.XPATH, "//*[text()= 'Zip/Postal Code']/parent::*/following-sibling::*/child::*").click()
        browser.find_element(By.XPATH, "//*[text()= 'Zip/Postal Code']/parent::*/following-sibling::*/child::*").send_keys("1945")
        browser.find_element(By.XPATH, "(//*[text()= 'Country']/parent::*/following-sibling::*/child::*/child::*/child::*)[2]").click()
        browser.find_element(By.XPATH, "//*[text()= 'Afghanistan']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)

    def test_organization_by_locations(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()='Organization ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Locations']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Name'])[1]/parent::*/following-sibling::*/child::*").send_keys("Texas R&D")
        browser.find_element(By.XPATH, "(//*[text()= 'City'])[1]/parent::*/following-sibling::*/child::*").send_keys("Texas")
        browser.find_element(By.XPATH, "((//*[text()= 'Country'])[1]/parent::*/following-sibling::*/child::*/child::*/child::*)[2]").click()
        browser.find_element(By.XPATH, "//*[text()= 'Afghanistan']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Search ']").click()
    
    def test_organization_by_structure(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()='Organization ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Structure']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Edit']/child::span").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Unit Id']/parent::*/following-sibling::*/child::*").send_keys("112233")
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)


unittest.main()