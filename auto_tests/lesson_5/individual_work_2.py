# На странице https://testautomationpractice.blogspot.com/

#1. Найти иконку Wikipedia по имени класса
#2. Найти поле ввода Wikipedia по id
#3. Найти кнопку поиска Wikipedia по классу
#4. Найти любой другой элемент на странице по тегу



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
#1. Найти иконку Wikipedia по имени класса
driver.find_element("class name", "wikipedia-icon")
#2. Найти поле ввода Wikipedia по id
driver.find_element("id", "Wikipedia1_wikipedia-search-input")
#3. Найти кнопку поиска Wikipedia по классу
driver.find_element("class name", "wikipedia-search-button")
#4. Найти любой другой элемент на странице по тегу
driver.find_element("tag name", "h2")