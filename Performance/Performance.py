import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class A_Performance(unittest.TestCase): 

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

    def test_a_MyTrackers(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #Menu Performance
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click() # Sub Menu MyTrackers
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[4]/div/button").click() # Button View
        time.sleep(3)

        #validation
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/h5").text

        self.assertEqual(responsedata, 'Tracker for paul')


    def test_b_KPIs(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #Menu Performance
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click() # Sub Menu Configure
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() # Sub Menu KPIs
        time.sleep(2)
        #dropdown
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div[1]").click()
        time.sleep(6)
        #memilih list dropdown
        for i in range (7) :
            browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys(Keys.ENTER)

        browser.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div").text
        self.assertEqual(responsedata, 'Database Administrator')
    
    def test_c_MyReviews(self):
        browser = self.browser
        browser.maximize_window()
        self.login()
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #Menu Performance
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click() # Klik Sub Manage Reviews
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]").click() # Klik My Reviews
        time.sleep(3)

        #validation
        responsedata = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/h6").text

        self.assertEqual(responsedata, 'My Reviews')

if __name__ == "__main__":
    unittest.main()