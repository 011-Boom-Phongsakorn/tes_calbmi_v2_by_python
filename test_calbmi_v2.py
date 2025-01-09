import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestCalBMI(unittest.TestCase):

    def setUp(self):
        # เปิด WebDriver
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1050, 840)
        self.driver.get("https://www.google.com/")

    def tearDown(self):
        # ปิด WebDriver
        time.sleep(2)
        self.driver.quit()

    def test_calbmi(self):
        # ค้นหาคำว่า "calculator bmi" บน Google
        search_box = self.driver.find_element(By.ID, "APjFqb")
        search_box.send_keys("calculator bmi")
        search_box.send_keys(Keys.RETURN)

        # รอให้ผลลัพธ์ค้นหาแสดงขึ้น
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ixcYae .LC20lb"))
        )

        # คลิกที่ลิงค์ที่นำไปสู่เครื่องคำนวณ BMI
        self.driver.find_element(By.CSS_SELECTOR, "#ixcYae .LC20lb").click()

        # รอให้ฟอร์มเครื่องคำนวณ BMI แสดง
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "cage"))
        )

        # ล้างข้อมูลเก่าในช่องกรอกข้อมูล
        self.driver.find_element(By.ID, "cage").clear()  # ล้างอายุ
        self.driver.find_element(By.ID, "cheightmeter").clear()  # ล้างส่วนสูง
        self.driver.find_element(By.ID, "ckg").clear()  # ล้างน้ำหนัก

        # กรอกข้อมูลต่างๆ สำหรับการคำนวณ BMI
        self.driver.find_element(By.ID, "cage").send_keys("20")  # อายุ
        self.driver.find_element(By.ID, "cheightmeter").send_keys("185")  # ส่วนสูง (185 cm)
        self.driver.find_element(By.ID, "ckg").send_keys("60")  # น้ำหนัก (60 kg)

        # คลิกปุ่มคำนวณ BMI
        self.driver.find_element(By.NAME, "x").click()

        # รอให้ผลลัพธ์ของ BMI แสดงขึ้น
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        # ตรวจสอบว่าผลลัพธ์ BMI ปรากฏขึ้น
        result = self.driver.find_element(By.ID, "result")
        print("BMI Result: " + result.text)

if __name__ == '__main__':
    unittest.main()
