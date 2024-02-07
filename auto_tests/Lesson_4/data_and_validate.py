import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url # PAGE_URL = driver.current_url # Получаем текущий URL-адрес в переменную
print("URL страницы", url)
assert url == "https://www.wikipedia.org/", "не та страница"

current_title = driver.title # Записываем значение title в переменную current_title
print("текущий заголовок", current_title) # Выводим значение переменной на экран
assert current_title == "Wikipedia", "не тот заголовок"


time.sleep(3)
# print(driver.print_page())# получение исходного кода станицы(для сравнения атрибутов, тегов, парсинга и т.д)