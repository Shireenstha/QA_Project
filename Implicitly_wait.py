from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up WebDriver options (optional)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

# Initialize WebDriver (Selenium Manager will handle ChromeDriver path)
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://demoblaze.com")

# Set implicit wait time
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be available

# Locate and interact with elements
nav_login = driver.find_element(By.ID, "login2")
nav_login.click()

uname = driver.find_element(By.ID, "loginusername")
uname.send_keys("testmorning")

pwd = driver.find_element(By.ID, "loginpassword")
pwd.send_keys("test123")

login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()

# Wait to observe the result (optional)
time.sleep(5)

# Close the browser
driver.quit()
