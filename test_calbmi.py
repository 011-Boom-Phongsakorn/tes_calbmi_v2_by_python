from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCalbmi():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_calbmi(self):
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(1050, 840)
    self.driver.find_element(By.ID, "APjFqb").click()
    self.driver.find_element(By.ID, "APjFqb").send_keys("calculator bmi")
    self.driver.find_element(By.NAME, "btnK").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ixcYae .LC20lb").click()
    self.driver.find_element(By.XPATH, "//li[@id=\'menuon\']/a").click()
    self.driver.find_element(By.ID, "cage").click()
    self.driver.find_element(By.ID, "cage").send_keys("20")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("185")
    self.driver.find_element(By.ID, "ckg").click()
    self.driver.find_element(By.ID, "ckg").send_keys("60")
    self.driver.find_element(By.NAME, "x").click()
  
