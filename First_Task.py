import time

from selenium import webdriver

# Function to get browser with specific URL
def get_browser_with_url(x):
    global driver  # Declare driver as global so we can use it throughout
    if x == 1:
        # Chrome Driver initialization, specify path if needed
        driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver
        driver.get("https://www.google.com/chrome/")  # Chrome URL
    elif x == 2:
        # Firefox Driver initialization, specify path if needed
        driver = webdriver.Firefox()  # Replace with the path to your GeckoDriver
        driver.get("https://www.mozilla.org/firefox/")  # Firefox URL
    elif x == 3:
        # Edge Driver initialization, specify path if needed
        driver = webdriver.Edge()  # Replace with the path to your EdgeDriver
        driver.get("https://www.microsoft.com/edge")  # Microsoft Edge URL
    else:
        print("Unknown browser selection.")
        return None
    return driver

# Prompt user for browser choice
print("Select a browser to open:")
print("1: Chrome")
print("2: Firefox")
print("3: Edge")

# Get the user's choice
try:
    choice = int(input("Enter your choice (1/2/3): "))
    browser = get_browser_with_url(choice)  # Call the function based on user input
    if browser:
        browser.maximize_window()  # Maximize the browser window
except ValueError:
    print("Invalid input. Please enter 1, 2, or 3.")
    time.sleep(5)
