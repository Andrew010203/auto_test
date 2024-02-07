import pickle  # библиотека для работы с куками
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# Логинимся в аккаунт
driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()

#____________________________сохраняем куки в файл___________________________________
# _________________что сохраняем____________куда сохраняем_________________операция__
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))
#_____________вернут все куки_______указатель места для записи или чтения___запись в бинарном формате__


# Чтобы больше не вводить каждый раз логин и пароль.Просто, перед тем как подставить/подгрузить куки, необходимо почистить все куки на странице, чтобы не было наложения.
# # Чистим все куки
# driver.delete_all_cookies()
#
# # Записываем куки из файла в переменную
# cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
#___________загрузка куки______указываем путь к файлу___________прочитать в бинарном формате__
#
#Так как куки это список словарей, нам необходимо добавлять куки по одной, чтобы не было проблем, соответсвенно тут мы используем простой цикл for для перебора списка:
# # Добавляем по одной куке из списка
# for cookie in cookies:
#     driver.add_cookie(cookie)
#
# # Делаем запрос на любую страницу залогиненного пользователя
# driver.get("https://www.freeconferencecall.com/profile")