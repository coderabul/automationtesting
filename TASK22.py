#2) To achieve this task, you can use the Selenium library in Python to automate the web browser and extract the required information from the Instagram page. First, make sure you have Selenium installed:

#pip install selenium
# Then, you need to download the appropriate WebDriver for your browser. In this example, I'll use the Chrome WebDriver. You can download it from here: https://sites.google.com/chromium.org/driver/

# Here's a sample script to extract the total number of followers and following from the specified Instagram profile:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver (make sure to provide the path to your webdriver executable)
driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

# Instagram profile URL
profile_url = 'https://www.instagram.com/guviofficial/'

# Open the Instagram profile page
driver.get(profile_url)
time.sleep(2)  # Wait for the page to load

# Find and click the 'Followers' link to open the followers list
followers_link = driver.find_element(By.XPATH, '//a[@href="/guviofficial/followers/"]')
followers_link.click()
time.sleep(2)  # Wait for the followers list to load

# Extract the total number of followers
followers_count = driver.find_element(By.XPATH, '//span[@class="g47SY"]').text
print(f'Total Followers: {followers_count}')

# Close the followers list
driver.find_element(By.XPATH, '//button[text()="Close"]').click()
time.sleep(1)  # Wait for the modal to close

# Find and click the 'Following' link to open the following list
following_link = driver.find_element(By.XPATH, '//a[@href="/guviofficial/following/"]')
following_link.click()
time.sleep(2)  # Wait for the following list to load

# Extract the total number of following
following_count = driver.find_element(By.XPATH, '//span[@class="g47SY"]').text
print(f'Total Following: {following_count}')

# Close the following list
driver.find_element(By.XPATH, '//button[text()="Close"]').click()

# Close the browser
driver.quit()