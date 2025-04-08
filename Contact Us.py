import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the given URL
driver.get("https://gb.bishalkarki.com/index.php?controller=order&ipa=4")

# Maximize the browser window to ensure all elements are visible
driver.maximize_window()

# Wait for the page to fully load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="contact-link"]/a'))
)

# Locate and click the "Contact Us" link
contact_us_link = driver.find_element(By.XPATH, '//*[@id="contact-link"]/a')
contact_us_link.click()

# Wait for the contact page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="message"]'))
)

# Scroll down the page to make sure the message box is visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

# Locate the message box
message_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="message"]'))
)

# Type the message in the message box
message_box.send_keys("I want three tops.")

# Optionally, you can add more steps such as submitting the form or navigating elsewhere.

# It's a good practice to add a brief pause before closing to see the outcome
time.sleep(5)

# Close the browser
driver.quit()
