from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_validation():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form = driver.find_elements(By.CSS_SELECTOR, "input.form-control")
    form[0].send_keys("Иван")
    form[1].send_keys("Петров")
    form[2].send_keys("Ленина, 55-3")
    form[4].send_keys("Россия")
    form[5].send_keys("Москва")
    form[6].send_keys("test@skypro.com")
    form[7].send_keys("+7985899998787")
    form[8].send_keys("QA")
    form[9].send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button").click()

    zip_code = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert zip_code == "alert py-2 alert-danger", \
        "Zip-code должен быть красным"

    list_id = [
        "#first-name",
        "#last-name",
        "#address",
        "#city",
        "#country",
        "#e-mail",
        "#phone",
        "#job-position",
        "#company",
    ]

    for i in list_id:
        class_element = driver.find_element(
            By.CSS_SELECTOR, i).get_attribute("class")
        assert class_element == "alert py-2 alert-success", \
            f"Поле {i} должно быть зелёным"

    driver.quit()
