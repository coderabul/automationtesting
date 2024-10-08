#1) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Wait for the search input field to be visible
search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "navbar-query"))
)

# Verify if the search input field is visible
if search_input:
    print("Successfully navigated to IMDb search page.")
else:
    print("Failed to navigate to IMDb search page.")

# Close the browser session
driver.quit()
#3) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")  # Replace with the actual URL

try:
    # Define an explicit wait
    wait = WebDriverWait(driver, 10)

    # Fill data in input boxes
    input_box1 = wait.until(EC.visibility_of_element_located((By.ID, "input-box1")))
    input_box1.send_keys("Data for input box 1")

    input_box2 = wait.until(EC.visibility_of_element_located((By.ID, "input-box2")))
    input_box2.send_keys("Data for input box 2")

    # Select options in select boxes
    select_box1 = wait.until(EC.visibility_of_element_located((By.ID, "select-box1")))
    select_box1.select_by_visible_text("Option 1")

    select_box2 = wait.until(EC.visibility_of_element_located((By.ID, "select-box2")))
    select_box2.select_by_value("option2")

    # Choose options in dropdown menus
    dropdown_menu1 = wait.until(EC.visibility_of_element_located((By.ID, "dropdown-menu1")))
    dropdown_menu1.click()
    dropdown_menu1_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Option 1']")))
    dropdown_menu1_option.click()

    dropdown_menu2 = wait.until(EC.visibility_of_element_located((By.ID, "dropdown-menu2")))
    dropdown_menu2.click()
    dropdown_menu2_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Option 2']")))
    dropdown_menu2_option.click()

    # Perform a search
    search_button = wait.until(EC.visibility_of_element_located((By.ID, "search-button")))
    search_button.click()

    print("Data filled in input boxes, select boxes, and dropdown menus. Search performed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser session
    driver.quit()
#2) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")  # Replace with the actual URL

try:
    # Define an explicit wait
    wait = WebDriverWait(driver, 10)

    # Fill data in input boxes
    input_box1 = wait.until(EC.visibility_of_element_located((By.ID, "input-box1")))
    input_box1.send_keys("Data for input box 1")

    input_box2 = wait.until(EC.visibility_of_element_located((By.ID, "input-box2")))
    input_box2.send_keys("Data for input box 2")

    # Select options in select boxes
    select_box1 = wait.until(EC.visibility_of_element_located((By.ID, "select-box1")))
    select_box1.select_by_visible_text("Option 1")

    select_box2 = wait.until(EC.visibility_of_element_located((By.ID, "select-box2")))
    select_box2.select_by_value("option2")

    # Choose options in dropdown menus
    dropdown_menu1 = wait.until(EC.visibility_of_element_located((By.ID, "dropdown-menu1")))
    dropdown_menu1.click()
    dropdown_menu1_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Option 1']")))
    dropdown_menu1_option.click()

    dropdown_menu2 = wait.until(EC.visibility_of_element_located((By.ID, "dropdown-menu2")))
    dropdown_menu2.click()
    dropdown_menu2_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Option 2']")))
    dropdown_menu2_option.click()

    # Perform a search
    search_button = wait.until(EC.visibility_of_element_located((By.ID, "search-button")))
    search_button.click()

    print("Data filled in input boxes, select boxes, and dropdown menus. Search performed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser session
    driver.quit()
#3) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")  # Replace with the actual URL

try:
    # Define an explicit wait
    wait = WebDriverWait(driver, 10)

    # Fill data in input boxes
    input_box1 = wait.until(EC.visibility_of_element_located((By.ID, "input-box1")))
    input_box1.send_keys("Data for input box 1")

    input_box2 = wait.until(EC.visibility_of_element_located((By.ID, "input-box2")))
    input_box2.send_keys("Data for input box 2")

    # Select options in select boxes
    select_box1 = wait.until(EC.element_to_be_clickable((By.ID, "select-box1")))
    select_box1.click()
    option1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Option 1']")))
    option1.click()

    select_box2 = wait.until(EC.element_to_be_clickable((By.ID, "select-box2")))
    select_box2.click()
    option2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Option 2']")))
    option2.click()

    # Choose options in dropdown menus
    dropdown_menu1 = wait.until(EC.element_to_be_clickable((By.ID, "dropdown-menu1")))
    dropdown_menu1.click()
    dropdown_menu1_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Option 1']")))
    dropdown_menu1_option.click()

    dropdown_menu2 = wait.until(EC.element_to_be_clickable((By.ID, "dropdown-menu2")))
    dropdown_menu2.click()
    dropdown_menu2_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Option 2']")))
    dropdown_menu2_option.click()

    # Perform a search
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "search-button")))
    search_button.click()

    print("Data filled in input boxes, select boxes, and dropdown menus. Search performed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser session
    driver.quit()
