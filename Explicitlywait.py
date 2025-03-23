from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver options (optional)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

# Initialize WebDriver (using Selenium Manager for ChromeDriver)
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://demoblaze.com")

# Set up WebDriverWait for explicit waits
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# Locate and interact with elements
nav_login = driver.find_element(By.ID, "login2")
nav_login.click()

# Wait until the username field is clickable and then interact
txt_box_username = wait.until(EC.element_to_be_clickable((By.ID, "loginusername")))
txt_box_username.send_keys("testmorning")

# Locate and send keys to the password field
txt_box_password = driver.find_element(By.ID, "loginpassword")
txt_box_password.send_keys("test123")

# Locate and click the login button
login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()

# Close the browser
driver.quit()
