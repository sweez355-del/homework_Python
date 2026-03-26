from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()


driver.get("http://uitestingplayground.com/textinput")


name_form = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys(
    "SkyPro"
)


blue_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_btn.click()

print(blue_btn.text)


driver.quit()
