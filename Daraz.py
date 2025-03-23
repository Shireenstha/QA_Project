from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome WebDriver (Ensure you have the correct WebDriver installed)
driver = webdriver.Chrome()

try:
    # Step 1: Open Daraz Nepal website
    driver.get("https://www.daraz.com.np/#?")
    time.sleep(3)  # Wait for page to load

    # Step 2: Locate the search input field using XPath and enter "dress"
    search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/input[1]")
    search_box.send_keys("dress")
    time.sleep(2)  # Wait before clicking search icon



    # Step 3: Click on the search icon
    search_icon = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div/div[2]/div/form/div/div[2]/a")
    search_icon.click()
    time.sleep(5)  # Wait for search results to load

    # Step 4: Click on the first dress image
    first_dress = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img")
    first_dress.click()
    time.sleep(5)  # Wait for product details page to load

    # Step 5: Scroll down slightly before adding to cart
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(3)  # Wait after scrolling

    # Step 6: Click "Add to Cart" button
    add_to_cart = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/div[2]/div/div[1]/div[17]/div/button[2]")
    add_to_cart.click()
    time.sleep(5)  # Wait for cart update

    # Step 7: Navigate to the cart page to verify if item is added
    driver.get("https://www.daraz.com.np/#?")
    time.sleep(5)  # Wait for cart page to load

    # Step 8: Check if the product is in the cart
    cart_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'cart-item')]")

    if cart_items:
        print("✅ Test Passed: Dress successfully added to cart.")
    else:
        print("❌ Test Failed: Dress not found in the cart.")

except Exception as e:
    print(f"❌ Test Execution Failed: {str(e)}")

finally:
    driver.quit()  # Close the browser
