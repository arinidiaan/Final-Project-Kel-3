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
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']")))).send_keys("Admin")
        # browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']")))).send_keys("admin123")
        # browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")))).click()
        # browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)

    def _a_project_report(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to project record
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/displayProjectReportCriteria")

        #input project name
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[1]/div/div/div//input[@placeholder='Type for hints...']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[1]/div/div/div//input[@placeholder='Type for hints...']").send_keys("Coca-cola")
        time.sleep(2)
        #select auto complete
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div//div[2]/div[1]/div[2]/div[1]").click()
        time.sleep(2)

        #pick date
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]//input[@placeholder='From']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]//input[@placeholder='From']").send_keys("2022-12-07")
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[2]//input[@placeholder='To']").send_keys("2022-12-18")
        time.sleep(2)

        #click view
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #check show record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//revo-grid//revogr-viewport-scroll[@class='rgCol']//revogr-overlay-selection[@type='rgRow']/revogr-data[@type='rgRow']/div")
        self.assertIn("("+str(len(record))+") Records Found",browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//span[@class='oxd-text oxd-text--span oxd-text--count']").text)

    def b_emp_report(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to employee record
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/displayEmployeeReportCriteria")

        #input emp name
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[1]/div/div/div//input[@placeholder='Type for hints...']").send_keys("Odis ")
        time.sleep(2)
        #auto complete
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div//div[2]/div[1]/div[2]/div[1]").click()
        time.sleep(2)

        #input project name
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]/div//input[@placeholder='Type for hints...']").send_keys("coca-cola ")
        time.sleep(2)
        #auto complete
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div//div[2]/div[1]/div[2]/div[1]").click()
        time.sleep(2)

        #click activity
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[2]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(2)
        #select menu ke 3
        for i in range (3) :
            browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        #pick date
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[3]/div/div[1]//input[@placeholder='From']").send_keys("2022-12-07")
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[3]/div/div[2]//input[@placeholder='To']").send_keys("2022-12-18")
        time.sleep(2)

        #click view
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #show record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//revo-grid//revogr-viewport-scroll[@class='rgCol']//revogr-overlay-selection[@type='rgRow']/revogr-data[@type='rgRow']/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
            print(toast.text)
            self.assertIn("No Records Found",toast.text)
            time.sleep(3)
        else:
            self.assertIn(browser.find_element("("+str(len(record))+") Records Found",By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//span[@class='oxd-text oxd-text--span oxd-text--count']").text)

    def test_c_attendance_summary(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to attendance summ
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[3]/a[@role='menuitem']").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/displayAttendanceSummaryReportCriteria")

        #input emp name
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Odis ")
        time.sleep(2)
        #auto complete
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div//div[2]/div[1]/div[2]/div[1]").click()
        time.sleep(2)


        #project name
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(2)
        #select menu ke 3
        for i in range (12) :
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        #sub unit
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        time.sleep(2)
        #select menu ke 3
        for i in range (13) :
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        #employee status
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        time.sleep(2)
        #select menu ke 3
        for i in range (3) :
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        #date range
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//input[@placeholder='From']").send_keys("2022-07-01")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//input[@placeholder='To']").send_keys("2022-07-30")
        time.sleep(2)
        
        #click view
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #show record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//revo-grid//revogr-viewport-scroll[@class='rgCol']//revogr-overlay-selection[@type='rgRow']/revogr-data[@type='rgRow']/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
            print(toast.text)
            self.assertIn("No Records Found",toast.text)
            time.sleep(3)
        else:
            self.assertIn(browser.find_element("("+str(len(record))+") Records Found",By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']//span[@class='oxd-text oxd-text--span oxd-text--count']").text)


 
    
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()