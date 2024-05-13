import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os

def get_value_from_excel(row, column):
    excel_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kd.xlsx")
    df = pd.read_excel(excel_file_path)
    value = df.iloc[row - 1, column - 1]
    return value

def get_xpath_from_excel(row, column):
    excel_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kd.xlsx")
    df = pd.read_excel(excel_file_path)
    xpath_value = df.iloc[row - 1, column - 1]
    return xpath_value

def is_element_present(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://glexas.com/hostel/login")
time.sleep(12)

for step in range(1, 15):
    xpath = get_xpath_from_excel(step, 4)
    value = get_value_from_excel(step, 5)
    if value:  # Check if value is not empty
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        if "select" in element.tag_name:
            select = Select(element)
            try:
                select.select_by_visible_text(value)
            except NoSuchElementException as e:
                print(f"Error selecting option '{value}': {e}")
        else:
            try:
                element.click()  # Click on the element to focus
                element.send_keys(value)
                # Check if the "to date" option is available after filling the field
                if step == 10 and not is_element_present(driver, get_xpath_from_excel(11, 4)):
                    print("Error: 'to date' option not available after selecting from dropdown.")
                    break  # Break out of the loop if "to date" option is not available
            except NoSuchElementException as e:
                print(f"Error: Element not found - {e}")
            except Exception as e:
                print(f"Error: {e}")
        time.sleep(2)

driver.find_element(By.XPATH, get_xpath_from_excel(14, 4)).click()
time.sleep(4)
