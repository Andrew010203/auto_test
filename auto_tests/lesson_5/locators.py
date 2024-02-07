import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://demoqa.com/automation-practice-form")

field_first_name = driver.find_element("xpath", '//input[@placeholder="First Name"]')
field_first_name.send_keys("Ivan")

field_last_name = driver.find_element("xpath", '//input[@placeholder="Last Name"]')
field_last_name.send_keys("Ivanov")

field_email = driver.find_element("xpath", '//input[@id="userEmail"]')
field_email.send_keys("Ivanov@mail.com")

radio_btn_gen = driver.find_element("xpath", '//label[@class="custom-control-label"]')
radio_btn_gen.click()

field_mobile_nbr = driver.find_element("xpath", '//input[@id="userNumber"]')
field_mobile_nbr.send_keys("555555555")

datepicker_field = driver.find_element("xpath", '//input[@id="dateOfBirthInput"]')
datepicker_field.clear()
# datepicker_field.send_keys("22/01/1994")

subjects_field = driver.find_element("xpath", '//input[@id="subjectsInput"]')
subjects_field.send_keys("En")
subjects_field.send_keys(Keys.TAB)
subjects_field.send_keys("His")
subjects_field.send_keys(Keys.TAB)
chbx_1 = driver.find_element("xpath", '//*[@id="hobbiesWrapper"]/div[2]/div[1]').click()
chbx_2 = driver.find_element("xpath", '//*[@id="hobbiesWrapper"]/div[2]/div[2]/label').click()


time.sleep(4)

