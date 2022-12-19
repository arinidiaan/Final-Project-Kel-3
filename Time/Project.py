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

    def test_a_project_report(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to customer menu
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/viewCustomers")

        #check show record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div/div[@role='row']")
        self.assertIn("("+str(len(record))+") Records Found",browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text)

    
    def test_b_add_cust(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to customer menu
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]").click()
        time.sleep(2)

        #click add
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/div/button[@type='button']").click()
        time.sleep(2)

        #input name
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//input").send_keys("PT. Indosat")
        time.sleep(2)

        #description
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//textarea[@placeholder='Type description here']").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,")
        time.sleep(2)

        #click save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #check toast
        toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
        self.assertIn("Success", toast.text)
        print(toast.text)
        time.sleep(3)
 
    def test_a_projects(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to projects menu
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]").click()
        time.sleep(2)

        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/time/viewProjects")

        #check show record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div/div[@role='row']")
        self.assertIn("("+str(len(record))+") Records Found",browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text)

        #search project
        #input customer name
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Coca-cola")
        time.sleep(2)
        #auto complete
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div//div[2]/div[1]/div[2]/div[1]").click()
        time.sleep(2)

        #input project
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Coke")
        time.sleep(2)
        #auto complete
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-autocomplete-wrapper']/div[2]/div[1]").click()
        time.sleep(2)

        #input project admin
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//div[@class='orangehrm-project-admin-input']/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Odis")
        time.sleep(2)
        #auto complete
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//div[@class='orangehrm-project-admin-input']/div//div[@class='oxd-autocomplete-wrapper']/div[2]/div[1]").click()
        time.sleep(2)

        #click view
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='orangehrm-background-container']/div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(2)

        #show record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
            print(toast.text)
            self.assertIn("No Records Found",toast.text)
            time.sleep(3)
        elif(len(record)== 1):
            self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text,"("+str(len(record))+") Record Found")
        else:
            self.assertIn("("+str(len(record))+") Records Found",browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text)



        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()