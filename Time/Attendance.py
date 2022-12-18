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

    def a_my_attendance(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to my records
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/viewMyAttendanceRecord")

        #pick a date
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.CONTROL,"a")
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.BACKSPACE)
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-18")
        time.sleep(3)

        #click view
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #cek show record
        #cek len record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div/div[@role='row']")

        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
            print(toast.text)
            self.assertIn("No Records Found",toast.text)
            time.sleep(3)
        else :
            self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//span[@class='oxd-text oxd-text--span']").text,"("+str(len(record))+") Records Found")

        
    def test_b_punch_in(self) :

        def pick__date_time(dates,times) :
            #pick a date
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[1]/div//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.CONTROL,"a")
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[1]/div//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.BACKSPACE)
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[1]/div//input[@placeholder='yyyy-mm-dd']").send_keys(dates)
            time.sleep(3)

            #pick a time
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[2]/div//input[@placeholder='hh:mm']").send_keys(Keys.CONTROL,"a")
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[2]/div//input[@placeholder='hh:mm']").send_keys(Keys.BACKSPACE)
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[2]/div//input[@placeholder='hh:mm']").send_keys(times)
            # time.sleep(3)

            #click In/Out
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
            time.sleep(3)

        browser = self.browser
        browser.maximize_window()
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to punch in
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]").click()
        time.sleep(2)

        #pre-cond belum punch in/sudah punch out
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")

        # #pick date n time
        # pick__date_time("2022-12-18", "07:00 AM")

        # #check go to punch out
        # self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchOut")

        # #pick date n time
        # pick__date_time("2022-12-18", "07:00 PM")

        # #check go to punch in
        # self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")

        # #cek toast success
        # toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
        # self.assertIn("Success",toast.text)

    def test_c_emp_record(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to attendance
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[3]/a[@role='menuitem']").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/viewAttendanceRecord")
        
        #isi nama empl
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div//input[@placeholder='Type for hints...']").send_keys("Paul")
        time.sleep(2)

        #auto complete wrapper
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div//div[2]/div[1]/div[2]/div[1]").click()
        time.sleep(2)

        #click view
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #cek show record
        #cek len record
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']")

        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
            print(toast.text)
            self.assertIn("No Records Found",toast.text)
            time.sleep(3)
        elif(len(record)== 1):
            self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//span[@class='oxd-text oxd-text--span']").text,"("+str(len(record))+") Record Found")
        else :
            self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//span[@class='oxd-text oxd-text--span']").text,"("+str(len(record))+") Records Found")


    def test_d_configure(self) :
        browser = self.browser
        self.login()
        browser.maximize_window()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to attendance
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[4]").click()
        time.sleep(2)
        #check url
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/configure")
        
        #toggle
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div[@class='oxd-switch-wrapper']//span").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div[@class='oxd-switch-wrapper']//span").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div[@class='oxd-switch-wrapper']//span").click()
        time.sleep(2)

        #click save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #check toast
        toast = browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-text--toast-message.oxd-toast-content-text")
        self.assertIn("Success", toast.text)
        print(toast.text)
        time.sleep(3)

    def test_e_punch_out(self) :

        def pick__date_time(dates,times) :
            #pick a date
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[1]/div//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.CONTROL,"a")
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[1]/div//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.BACKSPACE)
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[1]/div//input[@placeholder='yyyy-mm-dd']").send_keys(dates)
            time.sleep(3)

            #pick a time
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[2]/div//input[@placeholder='hh:mm']").send_keys(Keys.CONTROL,"a")
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[2]/div//input[@placeholder='hh:mm']").send_keys(Keys.BACKSPACE)
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[1]/div/div[2]/div//input[@placeholder='hh:mm']").send_keys(times)
            # time.sleep(3)

            #click In/Out
            browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
            time.sleep(3)

        browser = self.browser
        browser.maximize_window()
        self.login()

        #go to time menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/time/viewTimeModule']").click()
        time.sleep(2)

        #go to punch out
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[2]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[2]").click()
        time.sleep(2)

        #pre-cond sudah  punch in/belum punch out
        self.assertEqual(browser.current_url,"https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchOut")

        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()