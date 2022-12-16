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

class TestRecruitment(unittest.TestCase): 

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

    # def toRecruitmentMenu(self) :
    #     browser = self.browser
    #     browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
    #     time.sleep()

    def test_a_add_candidates_field_valid_data(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        self.login()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click() 
        time.sleep(3)
        #check url redirect
        get_url = browser.current_url
        self.assertEqual(get_url, 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate')

        #check first name field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]//input[@name='firstName']")))).send_keys("Jennie")
        #check middle name field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[2]//input[@name='middleName']")))).send_keys("Ruby")
        #check last name field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[3]//input[@name='lastName']")))).send_keys("Jane")
        #check dropdown menu
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div")))).click()
        # dropdown_menu = browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div[@class='oxd-select-dropdown --position bottom']/div[5]").click()
        browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys("Senior QA Lead")
        time.sleep(3)
        #check email field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//input[@placeholder='Type here']")))).send_keys("a@example.com")
        #check contact number field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div//input[@placeholder='Type here']")))).send_keys("085725100620")
        #check keyword field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[5]/div/div[1]/div//input[@placeholder='Enter comma seperated words...']")))).send_keys("Engineer")
        #check Note field
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[6]/div/div/div//textarea[@placeholder='Type here']")))).send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book")
        time.sleep(3)

        #check input invalid email
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(((By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//input[@placeholder='Type here']")))).send_keys("a@example.co!")
        self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div/span[.='Expected format: admin@example.com']").text,"Expected format: admin@example.com")


    def test_b_add_candidates_blank_email_name(self) :
        browser = self.browser
        browser.maximize_window()

        self.login()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        time.sleep(3)
        #click add
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        time.sleep(2)
        #click save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)
        #check required alert
        self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[1]/span[.='Required']").text,"Required")
        self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[3]/span[.='Required']").text,"Required")
        self.assertEqual(browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div/span[.='Required']").text,"Required")

    def a_browse_resume(self) :
        browser = self.browser
        browser.maximize_window()

        self.login()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        time.sleep(3)
        #click add
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        time.sleep(2)
        # browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[4]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/div//div[@class='oxd-file-button']").click()
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[4]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/div//div[@class='oxd-file-input-div']").send_keys("C:\\Arini\\QA Sanbercode\\Upload.txt")

    def test_c_pick_later_date(self) :
        browser = self.browser
        browser.maximize_window()

        self.login()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        time.sleep(3)
        #click add
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        time.sleep(2)

        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[5]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@placeholder='yyyy-mm-dd']").click()
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[5]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.CONTROL,"a")
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[5]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@placeholder='yyyy-mm-dd']").send_keys(Keys.BACKSPACE)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[5]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@placeholder='yyyy-mm-dd']").send_keys("2022-12-31")
        time.sleep(3)
        self.assertEquals(browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[5]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/span[.='Should be the current date or a previous date']"),"Should be the current date or a previous date")
        time.sleep(3)

    def test_d_save_candidate(self) :
        browser = self.browser
        # browser.maximize_window()

        # self.login()
        # browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        # time.sleep(3)
        # #click add
        # browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        # time.sleep(2)
        #isi data
        self.test_a_add_candidates_field_valid_data()
        #click save
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)
        # self.assertEqual(browser.find_element(By.XPATH,"//div[@id='oxd-toaster_1']/div").text, "Success")
        #check after save redirect to previous page
        get_url = browser.current_url
        self.assertEqual(get_url, 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate')
        




    def tearDown(self): 
        self.browser.close() 

   
if __name__ == "__main__": 
    unittest.main()