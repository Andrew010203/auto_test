import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# 1. Открыть 3 вкладки
#
# 2. Во вкладках перейти на страницы ниже страницы:
#
# Вкладка 1 - https://hyperskill.org/login
# Вкладка 2 - https://www.avito.ru/
# Вкладка 3 - https://www.ozon.ru/
# 3. Вывести в терминал title каждой страницы
# 4. Кликнуть на любую кнопку или ссылку на каждой странице
#
# Важно:
#
# Сначала нужно открыть все 3 вкладки
# Потом получить все title страниц
# Потом кликнуть на любой элемент в каждой вкладке

# открываем первую ссылку
driver.get("https://hyperskill.org/login")

# открываем вторую ссылку в новой вкладке
driver.switch_to.new_window("tab")
driver.get("https://www.avito.ru/")

# открываем третью ссылку в новой вкладке
driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru/")

# Выводим в терминал title каждой страницы
print(driver.window_handles)

# переключаемся на первую вкладку, находим любой элемент и кликаем на него
driver.switch_to.window(driver.window_handles[0])
driver.get("https://hyperskill.org/login")
ELEM_LOCATOR_1 = ("xpath", '//button[text()=" Start for free "]')
driver.find_element(*ELEM_LOCATOR_1).click()

# переключаемся на вторую вкладку, находим любой элемент и кликаем на него
driver.switch_to.window(driver.window_handles[1])
ELEM_LOCATOR_2 = ("xpath", '//a[@href="#login?authsrc=h"]')
driver.find_element(*ELEM_LOCATOR_2).click()

# переключаемся на третью вкладку, находим любой элемент и кликаем на него
driver.switch_to.window(driver.window_handles[2])
ELEM_LOCATOR_3 = ("xpath", '//button[@id="reload-button"]')
driver.find_element(*ELEM_LOCATOR_3).click()
time.sleep(7)


