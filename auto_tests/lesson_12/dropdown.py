import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown") # Страница для работы
DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
DROPDOWN.select_by_value("2")

# получить все значения списка из dropdown
# for option in all_options:
# DROPDOWN.select_by_value(option.get_attibute("value"))