# Задание 1 (Установка и чтение куки)
# 1. Откройте любой сайт и добавьте куки с именем "username" и значением "user123".
# 2. Затем обновите страницу и убедитесь, что кука "username" была успешно установлена.
# 3. Получите и провалидируйте значение куки "username" и выведете его на экран.




import pickle  # библиотека для работы с куками
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)


# Задание 3 (Автоматизация корзины покупок)
#   - Напишите сценарий, который использует Selenium WebDriver для автоматического добавления товаров в корзину, в интернет-магазине, например Amazon.
#   - После добавления товаров, сохраните состояние корзины, записав куки в переменную или файл.
#   - Затем удалите все товары из корзины, очистив все куки и перезагрузив страницу.
#   - Восстановите сессию путем подставления ранее сохраненных куков и перезагрузкой страницы после.
driver.get("https://altay.ru/")

# находим поле поиск и вписываем туда любое значение
poisk = driver.find_element("xpath", '//input[@id="title-search-input"]')
poisk.send_keys("Мумиё в капсулах")
poisk.click()

# для нахождения нужного элемента на странице применяем метод execute_script для скролла до нужного нам элемента
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# находим нужный товар и кликаем по нему
tovar = wait.until(EC.visibility_of(driver.find_element("xpath", '//a[@href="https://altay.ru/katalog/item/mumiye-v-kapuslakh/"]')))
tovar.click()

# находим кнопку добавления в корзину и нажимаем на нее
add = driver.find_element("xpath", '//a[@href="javascript:void(0);"]')
add.click()
#____________________________сохраняем куки в файл___________________________________
# _________________что сохраняем____________куда сохраняем_________________операция__
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# Чтобы больше не вводить каждый раз логин и пароль. Просто, перед тем как подставить/подгрузить куки, необходимо почистить все куки на странице, чтобы не было наложения.
# # Чистим все куки
driver.delete_all_cookies()

# # Записываем куки из файла в переменную
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
#___________загрузка куки______указываем путь к файлу___________прочитать в бинарном формате__
#
#Так как куки это список словарей, нам необходимо добавлять куки по одной, чтобы не было проблем, соответсвенно тут мы используем простой цикл for для перебора списка:
# # Добавляем по одной куке из списка
for cookie in cookies:
    driver.add_cookie(cookie)

# Делаем запрос на любую страницу залогиненного пользователя
driver.refresh()

# Добавляем куки
# driver.add_cookie({
#     "name": "username",
#     "value": "123"
# })
# # Получаем ранее добавленные куки
# print(driver.get_cookie("username"))

# Задание 2 (Удаление куков)
#   - Откройте любой сайт и через Devtools выберете куку.
#   - Удалите выбранную куку.
#   - После удаления куки, обновите страницу и проверьте, что она отсутствует.

# do = driver.get_cookie("_gid")
# print(do)
#
# driver.delete_cookie("_gid")
#
# driver.add_cookie({
#     "name": "_gid",
#     "value": "QWERTY"
# })
# posle = driver.get_cookie("_gid")
# print(posle)






