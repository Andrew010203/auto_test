# Задание 1:
# 1) Заполнить все текстовые поля данными (почистить поля перед заполнением).
# 2) Проверить, что данные действительно введены, используя get_attribute() и assert.


import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

field_full_name = driver.find_element("xpath", '//input[@placeholder="Full Name"]')
field_full_name.clear()
assert field_full_name.get_attribute('value') == ''
field_full_name.send_keys("Ivanov Ivan")
assert "Ivanov Ivan" in field_full_name.get_attribute('value')

field_email = driver.find_element("xpath", '//input[@id="userEmail"]')
field_email.clear()
assert field_email.get_attribute('value') == ''
field_email.send_keys("Ivan@mail.com")
assert "Ivan@mail.com" in field_email.get_attribute('value')

field_cur_address = driver.find_element("xpath", '//textarea[@id="currentAddress"]')
field_cur_address.clear()
assert field_cur_address.get_attribute('value') == ''
field_cur_address.send_keys("Moscow, Lenina 7")
assert "Moscow, Lenina 7" in field_cur_address.get_attribute('value')

field_perm_address = driver.find_element("xpath", '//textarea[@id="permanentAddress"]')
field_perm_address.clear()
assert field_perm_address.get_attribute('value') == ''
field_perm_address.send_keys("Volgograd, Gagarina 15")
assert "Volgograd, Gagarina 15" in field_perm_address.get_attribute('value')
time.sleep(5)

# Задание 2:
# 1) Прокликать все ссылки со статус-кодами на странице.
# 2) После каждого клика возвращаться на стартовую страницу.
driver.get(" http://the-internet.herokuapp.com/status_codes")

s_c_200 = driver.find_element("xpath", '//a[@href="status_codes/200"]')
s_c_200.click()
driver.back()

s_c_301 = driver.find_element("xpath", '//a[@href="status_codes/301"]')
s_c_301.click()
driver.back()

s_c_404 = driver.find_element("xpath", '//a[@href="status_codes/404"]')
s_c_404.click()
driver.back()

s_c_500 = driver.find_element("xpath", '//a[@href="status_codes/500"]')
s_c_500.click()
driver.back()


time.sleep(5)
