import random

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def extract_text(self, element):
        return element.text

    def zero_before_day(self, day):
        if int(day) <= 9:
            return f'0{day}'
        else:
            return day

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def action_move_to_element_click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def choose_random_element(self, elements_list, timeout=5):
        return elements_list[random.randint(0, len(elements_list) - 1)]