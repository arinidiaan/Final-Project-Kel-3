import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class A_LeaveList(unittest.TestCase):
    
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
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click()
    
    def test_a_search_leave_list(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("2022-11-01")
        time.sleep(1)
        
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("2022-12-31")
        time.sleep(1)
        
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)
        #select list
        for i in range (3) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]").click()

        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/span").text
        validation = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/span").text
        self.assertIn(response__data, validation)

    def test_b_approving_leave_req(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[9]/div/button[1]").click()
        time.sleep(1)

        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/span").text
        validation = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/span").text
        self.assertIn(response__data, validation)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

    def test_c_rejecting_leave_req(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[9]/div/button[2]").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

class B_AssignLeave(unittest.TestCase):
    
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
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click()
    
    def test_a_assign_leave(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[7]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Linda Jane Anderson")
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        time.sleep(1)

        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (5) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys("2022-12-26")
        time.sleep(1)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys("2022-12-29")
        time.sleep(1)
        
        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (2) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (2) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[6]/button").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.ID, "oxd-toaster_1")
        validation = browser.find_element(By.ID, "oxd-toaster_1")

        self.assertEqual(response__data, validation)

    def test_b_assign_leave_with_empty_employee_name(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[7]").click()
        time.sleep(1)

        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (5) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys("2022-12-26")
        time.sleep(1)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys("2022-12-29")
        time.sleep(1)
        
        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (2) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (2) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[6]/button").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/span").text
        self.assertIn('Required', response__data)

    def test_c_assign_leave_with_not_selecting_leave_type(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[7]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Linda Jane Anderson")
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[1]/input").send_keys("2022-12-26")
        time.sleep(1)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.DELETE)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys("2022-12-29")
        time.sleep(1)
        
        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (2) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (2) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[6]/button").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span").text
        self.assertIn('Required', response__data)

    def test_d_assign_leave_with_not_selecting_date(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[7]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Linda Jane Anderson")
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        time.sleep(1)

        #click dropdown
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(1)

        for i in range (5) :
            browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys(Keys.ENTER)
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[5]/button").click()
        time.sleep(1)

        #validation
        response__data = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/span").text
        self.assertIn('Required', response__data)
if __name__ == "__main__":
    unittest.main()
    