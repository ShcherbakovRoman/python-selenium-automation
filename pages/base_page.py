from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_elelment(self, *locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text: str, *locator):
        """
        Search for web element, get its text, compare with expected text
        :param expected_text: Text to be in web element
        :param locator: Searh strategy and locator of web element (e.g. (By.ID, 'id'0)
        """
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Error. Expected {expected_text} does not match actual {actual_text}'


    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))
