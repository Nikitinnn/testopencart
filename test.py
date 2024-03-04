from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера без указания пути к драйверу
driver = webdriver.Firefox()

# Открытие сайта
driver.get("https://demo.opencart.com/")

try:
        # 1. Кликнуть на продукт на главной странице, проверить переключение скриншотов на странице с продуктом.
        product_link = driver.find_element_by_css_selector(".product-layout:first-child .product-thumb")
        product_link.click()

        # Проверка переключения скриншотов на странице с продуктом
        screenshots = driver.find_elements_by_css_selector(".thumbnail")
        for screenshot in screenshots:
            screenshot.click()

        # 2. Сменить валюту на главной странице с доллара на евро и обратно.
        currency_dropdown = driver.find_element_by_css_selector("#form-currency")
        currency_dropdown.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'EUR'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'USD'))).click()

        # 3. Перейти через меню в категорию PC, проверить, что страница пуста.
        pc_category_link = driver.find_element_by_css_selector(
            "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a")
        pc_category_link.click()
        # Проверка, что страница пуста
        empty_page_message = driver.find_element_by_css_selector(".alert.alert-info")
        if empty_page_message.is_displayed():
            print("Страница категории 'PC' пуста.")
        else:
            print("Страница категории 'PC' не пуста.")

            # Пройти через меню в регистрацию
            registration_link = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?route=account/register']")
            registration_link.click()

            # Заполнение полей регистрации
            firstname_input = driver.find_element(By.ID, "input-firstname")
            firstname_input.send_keys("John")  # Здесь вводится имя пользователя

            lastname_input = driver.find_element(By.ID, "input-lastname")
            lastname_input.send_keys("Doe")  # Здесь вводится фамилия пользователя

            email_input = driver.find_element(By.ID, "input-email")
            email_input.send_keys("john.doe@example.com")  # Здесь вводится email пользователя

            telephone_input = driver.find_element(By.ID, "input-telephone")
            telephone_input.send_keys("1234567890")  # Здесь вводится номер телефона пользователя

            address_input = driver.find_element(By.ID, "input-address-1")
            address_input.send_keys("123 Main Street")  # Здесь вводится адрес пользователя

            city_input = driver.find_element(By.ID, "input-city")
            city_input.send_keys("Anytown")  # Здесь вводится город пользователя

            postcode_input = driver.find_element(By.ID, "input-postcode")
            postcode_input.send_keys("12345")  # Здесь вводится почтовый индекс пользователя

            country_input = driver.find_element(By.ID, "input-country")
            country_input.send_keys("United States")  # Здесь вводится страна пользователя

            region_input = driver.find_element(By.ID, "input-zone")
            region_input.send_keys("New York")  # Здесь вводится регион/штат пользователя

            # Нажатие кнопки "Зарегистрироваться"
            register_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
            register_button.click()


except Exception as e:
    print("Произошла ошибка:", e)

finally:
    # Закрытие браузера
    driver.quit()