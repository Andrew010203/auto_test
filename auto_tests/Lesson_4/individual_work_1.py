# 1.Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
# 2.Открыть любую страницу, например: vk.com.
# 3.Получить и вывести title в консоль.
# 4.Открыть любую другую страницу, например: ya.ru.
# 5.Получить и вывести title в консоль.
# 6.Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
# 7.Сделать рефреш страницы.
# 8.Получить и вывести URL-адрес текущей страницы.
# 9.Вернуться "вперед" на страницу из пункта 4.
# 10.Убедиться, что URL-адрес изменился.

import time
# 1.Инициализировать драйвер
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 2.Открыть любую страницу, например: vk.com.
driver.get("https://vk.com")

# 3.Получить и вывести title в консоль.
current_title = driver.title # Записываем значение title в переменную current_title
print("текущий заголовок", current_title) # Выводим значение переменной на экран
assert current_title == "ВКонтакте | Добро пожаловать", "не тот заголовок"

# 4.Открыть любую другую страницу, например: ya.ru.
driver.get("https://ya.ru.")

# 5.Получить и вывести title в консоль.
current_title = driver.title # Записываем значение title в переменную current_title
print("текущий заголовок", current_title) # Выводим значение переменной на экран
assert current_title == "Яндекс", "не тот заголовок"

# 6.Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
driver.back()
time.sleep(3)
url = driver.current_url # PAGE_URL = driver.current_url # Получаем текущий URL-адрес в переменную
print("URL страницы", url)
assert url == "https://vk.com/", "не та страница"

# 7.Сделать рефреш страницы.
driver.refresh()
time.sleep(3)
# 8.Получить и вывести URL-адрес текущей страницы.
url = driver.current_url
# 9.Вернуться "вперед" на страницу из пункта 4.
driver.forward()
time.sleep(3)
# 10.Убедиться, что URL-адрес изменился.
assert url == "https://vk.com/", "не та страница"
