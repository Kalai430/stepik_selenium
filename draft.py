import time # webdriver это и есть набор команд для управления браузером
from selenium import webdriver # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
try:
    driver = webdriver.Chrome()

    link="http://suninjuly.github.io/explicit_wait2.html"
    driver.get(link)

    price1 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button= driver.find_element(By.CSS_SELECTOR,'#book')
    button.click()

    x1 = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x = x1.text
    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    print(y)
    password = driver.find_element(By.CSS_SELECTOR, '#answer')  # Ищем поле для ввода пароля
    password.send_keys(y)  # Напишем текст в найденное поле

    button2 = driver.find_element(By.CSS_SELECTOR, '#solve')
    button2.click()

    time.sleep(30)

finally:
    driver.quit()