import time
from selenium import webdriver

PROXY = "37.19.220.129:8443"  # Указываем адрес прокси-сервера
#  Что если proxy-server требует авторизации? Все просто, перед IP-адресом прокси-сервера указываем логин и пароль в таком формате:
# PROXY = "username:password@37.19.220.129:8443"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://2ip.ru")  # Проверяем IP-адрес

time.sleep(5)