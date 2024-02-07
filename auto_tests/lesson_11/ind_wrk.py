from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/selectable")
# Переходим на вкладку "Grid"
grid = driver.find_element("xpath",'//a[@id="demo-tab-grid"]')
grid.click()

# Записываем локатор первого чек-бокса
six_ch_bx = ("xpath", '//*[@id="row2"]/li[3]')
do = driver.find_element(*six_ch_bx).get_attribute("class")
print(do)

# Кликаем на него
driver.find_element(*six_ch_bx).click()
posle = driver.find_element(*six_ch_bx).get_attribute("class")
print(posle)

one_ch_bx = ("xpath", '//*[@id="row1"]/li[1]')
do = driver.find_element(*one_ch_bx).get_attribute("class")
print(do)

# Кликаем на него
driver.find_element(*one_ch_bx).click()
posle = driver.find_element(*one_ch_bx).get_attribute("class")
print(posle)

# Проверяем, что после клика, к нему добавился класс active
assert "active" in posle
# if "active" in posle:
#     print("все хорошо")
# time.sleep(2)
# print(driver.find_element(*one_ch_bx).is_selected())
# time.sleep(2)
# driver.find_element(*one_ch_bx).click()
# time.sleep(2)
# print(driver.find_element(*one_ch_bx).is_selected())
# time.sleep(5)
