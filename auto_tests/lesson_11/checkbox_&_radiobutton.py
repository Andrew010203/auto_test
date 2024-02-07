from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Способ 1.Предлагает нам воспользоваться методом get_attribute(), но в этот раз нам нужно получить атрибут checked
driver.get("http://the-internet.herokuapp.com/checkboxes")

# Обьявляем локаторы
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

# Выполняем клик по первому чек-боксу
driver.find_element(*CHECKBOX_1).click()

# Убеждаемся что первый чек-бокс действительно выставлен
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None

# Выполняем клик по второму чек-боксу
driver.find_element(*CHECKBOX_2).click()

# Убеждаемся что второй чек-бокс действительно не выставлен
assert driver.find_element(*CHECKBOX_2).get_attribute("checked") is None

#При использовании get_attribute() нам будет возвращаться 2 значения:
#Если чек-бокс выставлен - True
#Если не выставлен - None


#Способ 2.Предлагает использовать новый метод is_selected(), который возвращает True, если флажок проставлен, и False, если не проставлен.
driver.get("http://the-internet.herokuapp.com/checkboxes")

CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

# Ставим флажок
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"

# Убираем флажок
driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"