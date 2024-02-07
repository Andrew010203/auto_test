import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
# 1. Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
btn_change_text = driver.find_element("xpath", '//button[@id="populate-text"]')
btn_change_text.click()
visible_after_btn = ("xpath", '//h2[text()="Selenium Webdriver"]')
wait.until(EC.visibility_of_element_located(visible_after_btn))

# Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
disp_btn_aft = driver.find_element("xpath", '//button[@id="display-other-button"]')
disp_btn_aft.click()
btn_enabled = ("xpath", '//button[@id="hidden"]')
wait.until(EC.visibility_of_element_located(btn_enabled))

# 3. Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”

en_btn_aft = driver.find_element("xpath", '//button[@id="enable-button"]')
en_btn_aft.click()
btn = ("xpath", '//button[@id="disable"]')
wait.until(EC.element_to_be_clickable(btn))

# 4. Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
clk_me_to_alert = driver.find_element("xpath", '//button[@id="alert"]')
clk_me_to_alert.click()
wait.until(EC.alert_is_present())