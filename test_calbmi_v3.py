import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestCalbmi(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1050, 840)

    def tearDown(self):
        time.sleep(2)  # อาจจะใช้เพื่อให้เห็นผลลัพธ์ก่อนปิดเบราว์เซอร์
        self.driver.quit()

    def test_calbmi(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.ID, "APjFqb").click()
        self.driver.find_element(By.ID, "APjFqb").send_keys("calculator bmi")
        self.driver.find_element(By.NAME, "btnK").click()
        self.driver.find_element(By.CSS_SELECTOR, "#ixcYae .LC20lb").click()
        # self.driver.find_element(By.ID, "menuon").click()
        self.driver.find_element(By.XPATH, "//li[@id='menuon']/a").click()

        # กรอกข้อมูล: อายุ, ความสูง, น้ำหนัก
        age_field = self.driver.find_element(By.ID, "cage")
        age_field.clear()  # ลบค่าเก่าก่อน
        age_field.send_keys("20")

        height_field = self.driver.find_element(By.ID, "cheightmeter")
        height_field.clear()  # ลบค่าเก่าก่อน
        height_field.send_keys("185")

        weight_field = self.driver.find_element(By.ID, "ckg")
        weight_field.clear()  # ลบค่าเก่าก่อน
        weight_field.send_keys("60")

        # คลิกปุ่มคำนวณ
        self.driver.find_element(By.NAME, "x").click()


if __name__ == '__main__':
    unittest.main()
