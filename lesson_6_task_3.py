from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.maximize_window()


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)


waiter = WebDriverWait(driver, 40)


waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)


image_container = driver.find_elements(By.CSS_SELECTOR, "#image-container img")


print(image_container[2].get_attribute("src"))


driver.quit()
