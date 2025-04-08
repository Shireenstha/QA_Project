from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.maximize_window()

wait = WebDriverWait(driver, 10)  # Configures the WebDriver to wait up to 10 seconds

try:
    # Open the Daraz Nepal website
    driver.get("https://www.daraz.com.np")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait until the page body is loaded

    # Locate the search input field by XPath and enter "dress"
    search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='q']")))
    search_box.send_keys("dress")

    # Click on the search icon
    search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='topActionHeader']/div[1]/div[2]/div/div[2]/div/form/div/div[2]/a")))
    search_icon.click()

    # Wait for search results to load and click on the specific party dress image
    first_dress = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div/a/div/img")))
    first_dress.click()

    # Switch to the new tab if it opens one
    driver.switch_to.window(driver.window_handles[-1])

    # Scroll down once to reveal the "Buy Now" button
    driver.execute_script("window.scrollTo(0, 600);")  # Adjust the scroll value as needed to ensure visibility of the button
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for scrolling effects

    # Click on the "Buy Now" button
    buy_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_add_to_cart']/div/button[1]")))
    buy_now_button.click()

    # Additional step to verify success or to proceed with checkout could be added here

    print("✅ Test Passed: Dress selected and 'Buy Now' clicked successfully.")

except Exception as e:
    print(f"❌ Test Execution Failed: {str(e)}")

finally:
    driver.quit()  # Close the browser
