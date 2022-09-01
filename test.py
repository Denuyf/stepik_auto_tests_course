from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    print("браузер открыт")
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    print("сайт открыт")
    WebDriverWait(browser, "12").until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print("ожидание добавлено")
    btn = browser.find_element(By.ID,"book").click()
    print("кнопка нажата")
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = math.log(math.fabs(12*math.sin(int(x.text))))
    print("расчеты произведены")
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    print("данные отправлены")
    time.sleep(5)
finally:
    browser.quit()
    print('браузер закрыт')
