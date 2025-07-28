from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=webdriver.ChromeOptions()
)
print("Window size:", driver.get_window_size())


driver.get('https://google.com')
print(driver.title)
driver.quit()


