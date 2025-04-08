import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://gb.bishalkarki.com/index.php?controller=order&ipa=4")
time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='contact-link']/a"))
)
contact_us_link = driver.find_element(By.XPATH, "//*[@id='contact-link']/a")
contact_us_link.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='message']"))
)
message = driver.find_element(By.XPATH, "//*[@id='message']")
message.send_keys("I want tops")
time.sleep(5)

driver.quit()
