import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://glexas.com/hostel/login")
time.sleep(10)

username_input = driver.find_element(By.XPATH, "//*[@id='username']")
username_input.send_keys("studenttest")

time.sleep(1)

password_input = driver.find_element(By.XPATH, "//*[@id='password']")
password_input.send_keys("studenttest")

time.sleep(1)

submit_button = driver.find_element(By.XPATH, "//*[@id='submit_button']")
submit_button.click()

time.sleep(1);
driver.find_element(By.XPATH,"//*[@id='header-toggle']").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/nav/div/div[5]/a").click()



driver.find_element(By.XPATH,"//*[@id='add']").click()
time.sleep(1)

titledd=driver.find_element(By.XPATH,"//*[@id='leave_main_id']")
title=Select(titledd)
title.select_by_visible_text("holiday")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='leave_place']").send_keys("Udaipur")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='reason']").send_keys("After continuously working for 15 days, I need a break for family trip")

date_input = driver.find_element(By.XPATH,"//*[@id='from_date']")
date_input.click()
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='from_date']").send_keys("11-05-2024")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='to_date']").send_keys("13-05-2024")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='from_time']").send_keys("09:30")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='to_time']").send_keys("11:00")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='parameterModalSubmit']").click()
time.sleep(4)
