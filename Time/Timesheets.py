from ctypes.wintypes import PINT
from distutils.core import setup
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestSearchCandidate(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def login(self) :
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']")))).send_keys("Admin")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin")
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']")))).send_keys("admin123")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123")
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")))).click()
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)

    def test_a_view_blank_employee(self) :
        browser = self.browser
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #click view button
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #cek required alert
        self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//div[@class='oxd-grid-item oxd-grid-item--gutters']/div/span[.='Required']").text,"Required")

    def test_b_edit_timesheet(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to my timesheet view
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]//i").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']").click()
        time.sleep(2)
        #cek redirect
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet")

        #click edit
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//div[@class='orangehrm-timesheet-footer--options']/button[@type='button']").click()
        time.sleep(2)

        #edit timesheet
        #reset
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[10]/button[@type='button']").click()
        #isi project
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Freewave")
        time.sleep(2)
        #auto complete wrapper
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//table/tbody/tr[1]/td[1]/div//div[@class='oxd-autocomplete-wrapper']/div[2]/div[1]/span").click()
        time.sleep(2)
        #click activity
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[2]/div//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        time.sleep(2)
        #select activity
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[2]/div//div[@class='oxd-select-wrapper']/div[2]/div[6]").click()
        time.sleep(2)
        #input timesheet
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[8]/div//input").send_keys(Keys.CONTROL,"a")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[8]/div//input").send_keys(Keys.BACKSPACE)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form//table/tbody/tr[1]/td[8]/div//input").send_keys("17:00")
        time.sleep(2)
        #click save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form//button[@type='submit']").click()
        time.sleep(2)


        #cek toast success
        toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']")
        self.assertIn("Success", toast[0].text)

    def test_c_view_employee_timesheet(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #input employee name
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Odis")
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-autocomplete-wrapper']/div[2]/div[1]").click()
        time.sleep(2)

        #click view
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #direct to page
        self.assertIn('Timesheet for ',browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//span[@class='oxd-text oxd-text--span']").text)

    def test_d_view_timesheet_pending(self) :
        browser = self.browser 
        browser.maximize_window()
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #get record ke 3
        record = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[3]/div[@role='row']")
        record_name = record.find_element(By.XPATH,".//div[1]/div").text
        
        #click view
        record.find_element(By.XPATH,".//div[3]//button[@type='button']").click()
        time.sleep(2)
        #harusnya OK kalau bahasanya sudah balik ke bahasa inggris
        self.assertIn("Timesheet for "+record_name, browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='orangehrm-background-container']/form//h6").text)
        
    def test_e_employee_timesheet(self) :
        browser = self.browser 
        browser.maximize_window()
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #click timesheet menu
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(2)
        #click  employee timesheet
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]").click()
        time.sleep(2)

        #cek redirect
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()