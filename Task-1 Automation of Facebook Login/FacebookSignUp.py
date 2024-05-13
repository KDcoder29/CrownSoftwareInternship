import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")


driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@name='firstname']").send_keys("Kandarp")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@name='lastname']").send_keys("Vaghela")
time.sleep(1)
driver.find_element(By.NAME, "reg_email__").send_keys("kandarp0629@gmail.com")
time.sleep(1)
try:
    reenter_email = driver.find_element(By.NAME, "reg_email_confirmation__")
    reenter_email.send_keys("kandarp0629@gmail.com")
except:
    pass
driver.find_element(By.NAME, "reg_passwd__").send_keys("kandarp0629")
time.sleep(1)


#DropDown Select
date = driver.find_element(By.ID, "day")
dateDD=Select(date)
dateDD.select_by_visible_text("2")
time.sleep(1)
dateDD.select_by_visible_text("6")

month = driver.find_element(By.ID, "month")
monthDD=Select(month)
monthDD.select_by_index(1)
time.sleep(0.1)
monthDD.select_by_value("3")
time.sleep(0.2)
monthDD.select_by_visible_text("Aug")

year=driver.find_element(By.ID,"year")
yearDD=Select(year)
yearDD.select_by_visible_text("2003")

driver.find_element(By.XPATH,"//*[text()='Male']").click()

driver.find_element(By.NAME,"websubmit").click()
time.sleep(10)
driver.quit()

# ddList = monthDD.options
# print(len(ddList))

# for ele in ddList:
#     print("Value is ",ele.text)
#     if ele.text=="Nov":
#         ele.click()
#         break

