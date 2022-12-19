import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class A_SearchEmployee(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)

    def test_a_search_employee_by_name(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Charlie")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text

        self.assertEqual(response__data, 'Charlie')

    def test_b_search_employee_by_id(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("0212")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").text

        self.assertEqual(response__data, '0212')

    def test_c_search_employee_by_nameandsupervisor(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Charlie")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input").send_keys("Aaliyah Haq")
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text
        self.assertEqual(response__data, 'Charlie')  

    def test_d_search_employee_by_nameandemploymentstatus(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(1)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Paul")
        time.sleep(1)
        #klik dropdown
        browser.find_element(By.XPATH, "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (3) :
            browser.find_element(By.XPATH, "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)

        browser.find_element(By.XPATH, "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)

        
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(1)

        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div").text

        self.assertIn('Full-Time Permanent', response__data) 

    def test_e_search_employee_with_invalid_nameandid(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Paol")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("0023")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)

        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/p[1]").text
        response__message = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/p[2]").text
        
        self.assertIn('Info', response__data)
        self.assertEqual(response__message, 'No Records Found')

class B_AddEmployee(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)

    def moveToPIMandAddEmployee(self):
        browser = self.browser
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click()
        time.sleep(2)


    def test_a_adding_employee(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        self.moveToPIMandAddEmployee()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Anto")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Maguire")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("Suryono")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)

        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

    def test_b_adding_employee_with_login_details(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        self.moveToPIMandAddEmployee()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Anto")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Maguire")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("Suryono")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("klangagus")

        status = "Enable"

        if status == "Enable":
            browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span").click()
            time.sleep(1)
        elif status == "Disable":
            browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label").click()
            time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("kinkjinK_009")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("kinkjinK_009")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

    def test_c_adding_employee_with_empty_last_name(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        self.moveToPIMandAddEmployee()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("Anto")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys("Maguire")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/span").text
        self.assertEqual(response__data, 'Required')

class C_Reports(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)

    def moveToPIMandReports(self):
        browser = self.browser
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/a[@href='#']").click()
        time.sleep(2)

    def test_a_make_new_reports(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(2)
        self.moveToPIMandReports()
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@placeholder='Type here ...']").send_keys("QWERTYS")
        time.sleep(1)

        #klik dropdown selection criteria
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div[2]/div[2]/button").click()
        time.sleep(1)

        #klik dropdown child selection criteria
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[4]/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[4]/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[4]/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        #klik dropdown include
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        #klik dropdown display fields group
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        #klik dropdown display fields
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div[2]/div[2]/button").click()
        time.sleep(1)

        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)   
    
    def test_b_search_reports(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(4)
        self.moveToPIMandReports()
        time.sleep(4)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("All Employee Sub Unit Hierarchy Report")
        time.sleep(3)
        browser.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #validation
        response__data = browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text
        self.assertIn("(1) Record Found",response__data)
    
    def test_c_open_reports(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(4)
        self.moveToPIMandReports()
        time.sleep(4)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button[3]").click()

        #validation
        response__data = browser.find_element(By.XPATH, "oxd-text oxd-text--h6 orangehrm-main-title")
        validation = browser.find_element(By.XPATH, "oxd-text oxd-text--h6 orangehrm-main-title")

        self.assertEqual(response__data, validation)
    
    def test_d_edit_reports_name(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(4)
        self.moveToPIMandReports()
        time.sleep(4)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button[2]").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").clear()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Changed Reports Name")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)
    
    def test_e_edit_reports_to_add_display_fields(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(4)
        self.moveToPIMandReports()
        time.sleep(4)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button[2]").click()
        time.sleep(3)

        #klik dropdown display fields group
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        #klik dropdown display fields
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(1)
        #select list
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[2]/div[1]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div[2]/div[2]/button").click()
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]").click()
        time.sleep(1)
        
        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

    def test_f_delete_reports(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(4)
        self.moveToPIMandReports()
        time.sleep(4)
        browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[3]/div/button[1]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

if __name__ == "__main__":
    unittest.main()