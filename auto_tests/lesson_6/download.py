import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads"
}
chrome_options.experimental_options["prefs"] = prefs
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#Задание 1. Загрузить любой файл в 'Choose File'.
# Страница для выполнения задания: https://demoqa.com/upload-download

driver.get("https://demoqa.com/upload-download")

upload_file_field = driver.find_element("xpath", '//input[@id="uploadFile"]')
upload_file_field.send_keys(f"{os.getcwd()}\downloads\(1).png")
time.sleep(3)

# Задание 2. С помощью цикла for скачать все файлы в папку lesson_6/downloads.
# Страница для выполнения задания: http://the-internet.herokuapp.com/download

driver.get("http://the-internet.herokuapp.com/download")
download_file = driver.find_elements("xpath", '//a')[3].click()
time.sleep(5)