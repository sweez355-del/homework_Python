from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()


driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(16)


blue_btn = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()


green_form = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(green_form)


driver.quit()
