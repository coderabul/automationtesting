#1) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start a new browser session
driver = webdriver.Chrome()

try:
    # Open the CoWIN website
    driver.get("https://www.cowin.gov.in/")

    # Wait for the page to load
    time.sleep(2)

    # Locate the "FAQ" anchor tag and click on it to open in a new window
    faq_link = driver.find_element(By.XPATH, "//a[contains(text(),'FAQ')]")
    faq_link.send_keys(Keys.CONTROL + Keys.RETURN)

    # Switch to the newly opened window
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the new page to load
    time.sleep(2)

    # Locate the "Partners" anchor tag and click on it to open in a new window
    partners_link = driver.find_element(By.XPATH, "//a[contains(text(),'Partners')]")
    partners_link.send_keys(Keys.CONTROL + Keys.RETURN)

    # Switch to the newly opened window
    driver.switch_to.window(driver.window_handles[2])

    # Wait for the new page to load
    time.sleep(2)

finally:
    # Close all windows
    driver.quit()
#2) 
from selenium import webdriver
import time

# Start a new browser session
driver = webdriver.Chrome()

try:
    # Open the CoWIN website
    driver.get("https://www.cowin.gov.in/")

    # Wait for the page to load
    time.sleep(2)

    # Locate the "FAQ" anchor tag and click on it to open in a new window
    faq_link = driver.find_element_by_xpath("//a[contains(text(),'FAQ')]")
    faq_link.click()

    # Wait for the new window to open
    time.sleep(2)

    # Fetch and display the opened window handles
    window_handles = driver.window_handles
    print("Opened Windows / Frame IDs:")
    for handle in window_handles:
        print(handle)

finally:
    # Close the browser session
    driver.quit()
#3) 
from selenium import webdriver
import time

# Start a new browser session
driver = webdriver.Chrome()

try:
    # Open the CoWIN website
    driver.get("https://www.cowin.gov.in/")

    # Wait for the page to load
    time.sleep(2)

    # Locate the "FAQ" anchor tag and click on it to open in a new window
    faq_link = driver.find_element_by_xpath("//a[contains(text(),'FAQ')]")
    faq_link.click()

    # Wait for the new window to open
    time.sleep(2)

    # Fetch the opened window handles
    window_handles = driver.window_handles

    # Switch to the newly opened window
    driver.switch_to.window(window_handles[1])

    # Close the FAQ window
    driver.close()

    # Switch back to the home page window
    driver.switch_to.window(window_handles[0])

    # Wait for a brief period
    time.sleep(2)

    # Locate the "Partners" anchor tag and click on it to open in a new window
    partners_link = driver.find_element_by_xpath("//a[contains(text(),'Partners')]")
    partners_link.click()

    # Wait for the new window to open
    time.sleep(2)

    # Fetch the opened window handles
    window_handles = driver.window_handles

    # Switch to the newly opened window
    driver.switch_to.window(window_handles[1])

    # Close the Partners window
    driver.close()

    # Switch back to the home page window
    driver.switch_to.window(window_handles[0])

finally:
    # Close the browser session
    driver.quit()
