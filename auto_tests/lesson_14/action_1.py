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
wait = WebDriverWait(driver, 10, poll_frequency=1) # Создаем обьект ожиданий
action = ActionChains(driver) # Создаем обьект action

# Шаг 1 - Открыть базовую страницу
driver.get("https://demoqa.com/buttons")
DOUBLE_CLICK_BTN_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
double_click_button = driver.find_element(*DOUBLE_CLICK_BTN_LOCATOR)
action.double_click(double_click_button).perform()
time.sleep(5)

# Тут все просто, но неочевидно! Для клика правой кнопкой мыши action использует метод context_click()

driver.get("https://demoqa.com/buttons")

RС_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")

BUTTON = driver.find_element(*RС_BUTTON_LOCATOR)

action.context_click(BUTTON).perform()


# #Все переменные Step это просто для понимания как работает именно цепочка действий, действие за действием.
#
# driver.get("https://demoqa.com/menu")
#
# STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
# STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
# STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")
#
# STEP_1 = driver.find_element(*STEP_1_LOCATOR)
# STEP_2 = driver.find_element(*STEP_2_LOCATOR)
# STEP_3 = driver.find_element(*STEP_3_LOCATOR)
#
# action.move_to_element(STEP_1) \ # Наведение не пункт меню
#     .move_to_element(STEP_2) \ # Наведение на подпункт,если требуется можно делать паузу .pause(2)\
#     .click(STEP_3) \ # Клик на подпункт
#     .perform() # Выполнить
#
# time.sleep(5)
# #Символ / в коде, это просто перенос на другую строку, иначе длина строки будет огромной)


# # Пишем код для перетаскивания.
#
# driver.get("https://demoqa.com/droppable")
#
# SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
# TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")
#
# SOURCE = driver.find_element(*SOURCE_LOCATOR)
# TARGET = driver.find_element(*TARGET_LOCATOR)
#
# wait.until(EC.element_to_be_clickable(SOURCE))
# action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскивание
#
# time.sleep(5)


# #Реализуем саму функцию, она будет принимать в себя 2 локатора и перетаскивать элементы:
#
# driver.get("https://demoqa.com/sortable")
#
# SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
# TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")
#
# def drag_and_drop(source, target):
#     SOURCE = driver.find_element(*source) # Находим source-элемент
#     TARGET = driver.find_element(*target) # Находим target-элемент
#     wait.until(EC.element_to_be_clickable(SOURCE)) # Ждем кликабельности source-элемента
#     action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскиваем
#
# drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR) # Использование функции


# #Содержимое файла "scrolls.py":
#
# class Scrolls:
#
#     def __init__(self, driver, action):
#         self.driver = driver
#         self.action = action
#
#     def scroll_by(self, x, y): # Скролл по x и y
#         self.driver.execute_script(f"window.scrollTo({x}, {y})")
#
#     def scroll_to_bottom(self): # Скролл в самый низ страницы
#         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#
#     def scroll_to_top(self): # Скролл на самый верх страницы
#         self.driver.execute_script("window.scrollTo(0, 0)")
#
#     def scroll_to_element(self, element):# Скролл к элементу с раскрытием контента под ним
#         self.action.scroll_to_element(element).perform()
#         self.driver.execute_script("""
#         window.scrollTo({
#             top: window.scrollY + 700,
#         });
#         """)