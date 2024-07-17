# whatsapp.py

import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def open_whatsapp():
    # Initialize Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\kaush\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com')
    time.sleep(30)  # Give some time to load

    if not is_logged_in(driver):
        print("Please scan the QR code to log in to WhatsApp Web.")
        time.sleep(20)  # Wait for the user to scan the QR code and log in

    # Check again if logged in
    if not is_logged_in(driver):
        print("Not logged in. Exiting.")
        driver.quit()
        return

    print("Logged in successfully.")

def is_logged_in(driver):
    
    try:
        driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        return True
    except NoSuchElementException:
        return False

def send_message(contact_name, message):
    # Example: Search for the contact and send the message
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    time.sleep(1)
    search_box.send_keys(contact_name)
    time.sleep(2)  # Wait for search results to appear
    search_box.send_keys(Keys.ENTER)
    
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    
    # Close the browser after sending message
    time.sleep(5)
    driver.quit()
