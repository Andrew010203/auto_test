import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
# Запуск браузера с заданным разрешением
options.add_argument("--window-size=1920,1080")
# Отключение средства автоматизации т.е. браузером управляет человек
options.add_argument("--disable-blink-features=AutomationControlled")
# Запуск браузера с игнорированием ssl сертификатов
options.add_argument("--ignore-certificate-errors")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")

time.sleep(5)