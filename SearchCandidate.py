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

    def test_a_search_by_job_title(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
        #click dropdown menu
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(3)
        #select menu
        option = browser.find_elements(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]//div[@class='oxd-select-wrapper']/div[2]/div[@class='oxd-select-option']/span")
        for i in range (len(option)) :
            if option[i].text == "QA Lead" :
                option[i].click()
                break
        time.sleep(3)

        #cara lain select menu
        #select menu ke 5
        # for i in range (5) :
        #     browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        # time.sleep(3)
        # browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[2]/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            for i in range (len(record)) :
                #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
                self.assertIn("QA Lead", record[i].text)
                print(record[i].text)

        time.sleep(3)


    def test_b_search_by_vacancy(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
        
        #click dropdown menu
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(3)
        #select menu
        option = browser.find_elements(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]//div[@class='oxd-select-wrapper']/div[2]/div[@class='oxd-select-option']/span")
        for i in range (len(option)) :
            if option[i].text == "Senior QA Lead" :
                option[i].click()
                break
        time.sleep(3)

        #cara lain select menu
        #select menu ke 5
        # for i in range (5) :
        #     browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        # time.sleep(3)
        # browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[2]/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            for i in range (len(record)) :
                #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
                self.assertIn("Senior QA Lead", record[i].text)
                print(record[i].text)

        time.sleep(3)

    def test_c_search_by_hiring_manager (self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
        
        #click dropdown menu
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[1]/div/div[3]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]").click()
        #select menu
        option = browser.find_elements(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]//div[@class='oxd-select-wrapper']/div[2]/div[@class='oxd-select-option']/span")
        
        for i in range (len(option)) :
            if option[i].text == "Odis Adalwin" :
                option[i].click()
                break
        time.sleep(3)

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)
        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[4]/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            for i in range (len(record)) :
                #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
                self.assertIn("Odis Adalwin", record[i].text)
                print(record[i].text)

        time.sleep(3)

    def test_d_search_by_status(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
    
        #click dropdown menu
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(3)
        #select menu
        option = browser.find_elements(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]//div[@class='oxd-select-wrapper']/div[2]/div[@class='oxd-select-option']/span")
        for i in range (len(option)) :
            if option[i].text == "Rejected" :
                option[i].click()
                break
        time.sleep(3)

        #cara lain select menu
        #select menu ke 5
        # for i in range (5) :
        #     browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        # time.sleep(3)
        # browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[6]/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            for i in range (len(record)) :
                #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
                self.assertIn("Rejected", record[i].text)
                print(record[i].text)

        time.sleep(3)

    def test_e_search_by_candidate_name(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
    
        #click text box
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("Chris")
        time.sleep(3)
        #select menu
        option = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]/div/div[1]/div//div[@class='oxd-autocomplete-wrapper']/div[2]/div[@role='option']/span")
        for i in range (len(option)) :
            if option[i].text == "Chris Harris" :
                option[i].click()
                break
        time.sleep(3)

        #cara lain select menu
        #select menu ke 5
        # for i in range (5) :
        #     browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        # time.sleep(3)
        # browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[3]/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            for i in range (len(record)) :
                #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
                self.assertIn("Chris", record[i].text)
                print(record[i].text)

        time.sleep(3)

    def test_f_search_by_keyword(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
    
        #click text box
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//input[@placeholder='Enter comma seperated words...']").send_keys("Lorem ipsum")
        time.sleep(3)
        
        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[3]/div")
        for i in range (len(record)) :
            #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
            self.assertIn("Lorem ipsum", record[i].text)
            print(record[i].text)
        
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            self.assertIn("("+(str(len(record)))+") Records Found",browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text)


    def test_g_search_by_date(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
    
        #click text box
        #From date
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]//input[@placeholder='From']").send_keys("2022-07-01")
        time.sleep(3)
        #To date
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[2]//input[@placeholder='To']").send_keys("2022-07-31")

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[5]/div")
        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            for i in range (len(record)) :
                #soalnya listnya bisa ganti2, jadi expectednya bisa aja berubah
                self.assertIn("2022-07-", record[i].text)
                print(record[i].text)
    
    def test_h_search_by_method(self) :
        browser = self.browser
        browser.maximize_window()
        self.login()
        #go to recruitment menu
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        time.sleep(3)
    
        #click text box
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[3]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/div[2]/div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        time.sleep(3)
        
        #select menu
        option = browser.find_elements(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[3]/div/div//div[@class='oxd-select-wrapper']/div[2]/div[@class='oxd-select-option']/span")
        
        for i in range (len(option)) :
            if option[i].text == "Online" :
                option[i].click()
                break
        time.sleep(3)

        #click search
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)

        #cek hasil pencarian di record seharusnya ada yang valuenya sesuai yg dipilih 
        record = browser.find_elements(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[1]/div")

        #check jika tidak ada record
        if (len(record) == 0) :
            toast = browser.find_elements(By.XPATH,"//div[@id='oxd-toaster_1']//div[@class='oxd-toast-start']/div[2]/p")
            print(toast[0].text)
            print(toast[1].text)
            self.assertIn("Info",toast[0].text)
            self.assertIn("No Records Found",toast[1].text)
            time.sleep(3)
        else :
            self.assertIn("("+(str(len(record)))+") Records Found",browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text)


        

        #check jika ada record
        



    def tearDown(self): 
        self.browser.close() 


 
if __name__ == "__main__": 
    unittest.main()

