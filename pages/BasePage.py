import random
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def zero_before_day(self, day):
        if int(day) <= 9:
            return f'0{day}'
        else:
            return day

    def click_element(self, element):
        element.click()

    def element_send_keys(self, locator, keys):
        return self.driver.find_element(locator).send_keys(keys)

    def action_move_to_element_click(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator)
        action.click()
        action.perform()

    def choose_random_element(self, elements_list):
        return elements_list[random.randint(0, len(elements_list) - 1)]

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
