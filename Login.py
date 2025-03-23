import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (Ensure you have the correct driver version installed)
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the URL
driver.get("https://gb.bishalkarki.com/admin123/index.php?controller=AdminLogin&token=f03074c5517053da9800293c3b31d076&redirect=AdminOrders")

# Wait for the page to load
time.sleep(3)

# Locate the email field and input the email
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys("admin@gb.bishalkarki.com")

# Locate the password field and input the password
password_field = driver.find_element(By.XPATH, '//*[@id="passwd"]')
password_field.send_keys("Test123!@#")

# Locate the login button and click it
login_button = driver.find_element(By.XPATH, '//*[@id="login_form"]/div[3]/button')
login_button.click()

# Optional: Wait for a few seconds to observe the login result
time.sleep(5)

# Close the browser
driver.quit()
