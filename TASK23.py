from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the webdriver (make sure to provide the path to your webdriver executable)
driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

# Open the URL
url = 'https://jqueryui.com/droppable/'
driver.get(url)
time.sleep(2)  # Wait for the page to load

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

# Find the draggable element (White Box)
draggable_element = driver.find_element(By.ID, 'draggable')

# Find the droppable element (Yellow Rectangular Box)
droppable_element = driver.find_element(By.ID, 'droppable')

# Use Action Chains to perform the Drag and Drop operation
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Switch back to the default content
driver.switch_to.default_content()

# Wait for a moment to see the result
time.sleep(2)

# Close the browser
driver.quit()
