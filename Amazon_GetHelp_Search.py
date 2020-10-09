from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/romanshcherbakov/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

input_field = driver.find_element(By.ID, 'helpsearch')
input_field.send_keys('Cancel Order', Keys.ENTER)


result = driver.find_element(By.XPATH, "//a[contains(@href, 'GSL')]")
# ("//h1[@text()='Cancel Items or Orders']")

assert result.text == 'Cancel Items or Orders', f'Error. Expected Cancel Items or Orders but got {result.text}'

driver.quit()