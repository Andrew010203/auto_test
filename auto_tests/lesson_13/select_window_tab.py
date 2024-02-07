import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1.Открыть какую-то базовую страницу
# 2.Открыть несколько вкладок
# 3.Получить их количество
# 4.Получить дескриптор открытой вкладки
# 5.Переключиться на любую вкладку используя ее индекс
# 6.Проверить, что вкладка переключилась

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)

# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows)) # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)

# Шаг 6 - Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"

# # Шаг 1 - Открыть базовую страницу
# driver.get("https://whatismyipaddress.com/")
#
# # Шаг 2 - Получение дескриптора текущего окна
# old_window = driver.current_window_handle
# print("Дескриптор первого окна: ", old_window)
#
# # Шаг 3 - Открытие и переключение на новое окно
# driver.switch_to.new_window("window")
#
# # Шаг 4 - Получение дескриптора нового окна
# new_window = driver.current_window_handle
# print("Дескриптор второго окна: ", new_window)
#
# # Шаг 5 - Проверка, что окно переключилось
# assert new_window == driver.current_window_handle, "Окно не переключилось"
# time.sleep(2)
#
# # Шаг 6 - Открытие страницы в новом окне
# driver.get("https://vk.com")
#
# # Шаг 7 - Переключение на старое окно
# driver.switch_to.window(old_window)
#
# # Шаг 8 - Проверка, что переключились на старое окно
# assert old_window == driver.current_window_handle, "Окно не переключилось"
#
# # Шаг 9 - Открытие страницы в старом окне
# driver.get("https://ya.ru")
#
# # Шаг 10 - Переключение на новое окно
# driver.switch_to.window(new_window)
#
# # Шаг 11 - Закрытие нового окна
# driver.close()