#1.Certainly! Below is a Python script using Selenium to perform the specified tasks: displaying cookies before and after login on https://www.saucedemo.com/, logging in, and then logging out.

from selenium import webdriver

# Function to display cookies
def display_cookies(driver):
    cookies = driver.get_cookies()
    print("Cookies:")
    for cookie in cookies:
        print(f"{cookie['name']}: {cookie['value']}")
    print()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the Saucedemo website
    driver.get("https://www.saucedemo.com/")

    # Display cookies before login
    print("Before Login:")
    display_cookies(driver)

    # Login
    username = "standard_user"
    password = "secret_sauce"

    driver.find_element_by_id("user-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()

    # Display cookies after login
    print("After Login:")
    display_cookies(driver)

    # Logout
    driver.find_element_by_id("react-burger-menu-btn").click()
    driver.find_element_by_id("logout_sidebar_link").click()

    # Display cookies after logout
    print("After Logout:")
    display_cookies(driver)

finally:
    # Close the browser window
    driver.quit()
# This script uses the Chrome WebDriver, so make sure you have the ChromeDriver executable in your system's PATH or specify its location. You can download ChromeDriver from https://sites.google.com/chromium.org/driver/.

# Replace the username and password variables with your valid credentials for the Saucedemo website.

# This script does the following:

# Opens the Saucedemo website.
# Displays cookies before login.
# Logs in with the provided credentials.
# Displays cookies after login.
# Logs out.
# Displays cookies after logout.