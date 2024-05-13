from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Load the Excel file
excel_file = 'task4.xlsx'
web_sheet = 'Web'
main_sheet = 'Main'

# Load data from Excel into DataFrames
web_df = pd.read_excel(excel_file, sheet_name=web_sheet)
main_df = pd.read_excel(excel_file, sheet_name=main_sheet)

# Start WebDriver
driver = webdriver.Chrome()  # Change this to your preferred WebDriver
driver. maximize_window()

# Open the website
driver.get('https://glexas.com/hostel/login')
time.sleep(10)  # Adjust the sleep time as needed based on page load time

# Iterate through rows in the main sheet
for main_index, main_row in main_df.iterrows():
    main_title = main_row['Title/ld']

    # Find corresponding rows in the web sheet
    web_rows = web_df[web_df['Title/ld'] == main_title]

    # Now perform actions based on the matched title
    for _, web_row in web_rows.iterrows():
        xpath = web_row['X path/url/ID']
        value = web_row['value']

        # Skip iteration if value is 'event visit'
        if value == 'event visit':
            continue

        # Perform actions based on value
        if pd.isnull(value):  # If value is null, click the element
            # Wait for the element to be clickable
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            time.sleep(1)  # Optional: Add a short delay after clicking
        else:  # If value is not null, send keys to the element
            # Wait for the element to be clickable
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.send_keys(value)
            time.sleep(1)  # Optional: Add a short delay after sending keys

# Close the browser
driver.quit()
