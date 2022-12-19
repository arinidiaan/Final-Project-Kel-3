import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class A_ContactDetails(unittest.TestCase): 

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text

        self.assertEqual(responsedata, 'Dashboard')

    def test_Contact_Details(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Menu My Info
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click() # Sub Menu Contact Details
        time.sleep(2)
        #Data Street 1
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Olympus")
        time.sleep(2)
        # Input Data Nomor Telephone Mobile
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("+61485872892")
        time.sleep(2)
        #Menghpaus email 
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/input").send_keys(Keys.DELETE)
        time.sleep(2)
        #Isi data email 
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/input").send_keys("Olympus@gmail.com")
        time.sleep(2)
        #Click button save
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()
        time.sleep(5)

        #validation
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

    def test_Delete_Street1(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Menu My Info
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click() # Sub Menu Contact Details
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.DELETE)
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()
        time.sleep(3)

        #validation
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

    def test_Delete_MobileNumber(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Menu My Info
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click() # Sub Menu Contact Details
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[2]/div/div[2]/input").send_keys(Keys.DELETE)
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()
        time.sleep(3)

        #validation
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

    def test_Delete_Email(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Menu My Info
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click() # Sub Menu Contact Details
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[3]/div/div[1]/div/div[2]/input").send_keys(Keys.DELETE)
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()
        time.sleep(3)

        #validation
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

class B_EmergencyContacts(unittest.TestCase):

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_a_EmergencyContactsRequiredPhoneNumber(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Klik menu My info
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click() #Klik sub menu EmergencyContact
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click() #klik button +Add
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Erick") #input nama
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Friends") #input relationship
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click() #button save
        time.sleep(7)

        #validation
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/span").text
        self.assertEqual(responsedata, 'At least one phone number is required')

    def test_b_EmergencyContactsRequiredRelationship(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Klik menu My info
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click() #Klik sub menu EmergencyContact
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click() #klik button +Add
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Erick") #input nama
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("07700 900111") #input nomor telephone
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click() #button save
        time.sleep(7)

        #validation
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/span").text
        self.assertEqual(responsedata, 'Required')
    
    def test_c_EmergencyContacts(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Klik menu My info
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click() #Klik sub menu EmergencyContact
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click() #klik button +Add
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Erick") #input nama
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Friends") #input relationship
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("07700 900111") #input nomor telephone
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click() #button save
        time.sleep(7)

        #validation
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").text
        self.assertEqual(responsedata, 'Erick')


class C_Dependents(unittest.TestCase): 

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

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')
    
    def test_a_Dependents_Required_Relationship(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Hamilton")
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()
        time.sleep(3)
        
        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/span").text
        self.assertEqual(responsedata, 'Required')

    def test_b_AddDependents(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Aaron")
        time.sleep(3)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']")
        time.sleep(1)
        for i in range (2) :
            browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[3]/div/div[2]/input").send_keys("Wife")
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()
        time.sleep(3)


        #validasi
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

class D_Immigration(unittest.TestCase):

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

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_Immigrations_sukses(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/div/label").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").send_keys("039677847")
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()
        time.sleep(5)

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text
        self.assertEqual(responsedata, '039677847')

class E_Job(unittest.TestCase):

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_JobDetails(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
        time.sleep(4)

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text
        self.assertEqual(responsedata, 'Job Details')

class F_Salary(unittest.TestCase):

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_Salary(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a").click()
        time.sleep(4)

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/h6").text
        self.assertEqual(responsedata, 'Assigned Salary Components')

class G_Tax(unittest.TestCase):

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_Tax(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a").click()
        time.sleep(4)

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text
        self.assertEqual(responsedata, 'Tax Exemptions')

class H_Report(unittest.TestCase):

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_Report_to(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a").click()
        time.sleep(4)

        #validasi
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text
        self.assertEqual(responsedata, 'Report to')

class I_Qualification(unittest.TestCase):

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        self.assertEqual(responsedata, 'Dashboard')

    def test_Add_WorkExperience(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Red Bull Racing Formula One Team")
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("FINANCIAL ACCOUNTANT")
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[4]/button[2]").click()
        time.sleep(4)

        #validasi
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

class J_PersonalDetails(unittest.TestCase): 

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

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text

        self.assertEqual(responsedata, 'Dashboard')

    def test_a_ChangeGender(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click() #Menu My Info
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a").click() # Sub Menu Personal Details
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()
        time.sleep(5)
        #validation
        responsedata = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(responsedata, validation)

if __name__ == "__main__":
    unittest.main()