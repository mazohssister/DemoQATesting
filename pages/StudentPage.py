import os
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from pages.BasePage import BasePage


class StudentPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER_RADIO_MALE = (By.XPATH, "//input[@id='gender-radio-1']")
    GENDER_RADIO_FEMALE = (By.XPATH, "//input[@id='gender-radio-2']")
    GENDER_RADIO_OTHER = (By.XPATH, "//input[@id='gender-radio-3']")
    ALL_GENDER_RADIO = (By.XPATH, "//input[@name='gender']")
    ALL_MONTHS_DATE_OF_BIRTH = (By.XPATH, "//select[@class='react-datepicker__month-select']/option")
    ALL_YEAR_DATE_OF_BIRTH = (By.XPATH, "//select[@class='react-datepicker__year-select']/option")
    CLICK_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    CLICK_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")
    DATE_OF_BIRTH_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    SUBJECTS = (By.XPATH, "//input[@id='subjectsInput']")
    ALL_HOBBIES = (By.XPATH, "//div[@id='hobbiesWrapper']//child::input[@type='checkbox']")
    HOBBIES_1 = (By.XPATH, "//input[@id='hobbies-checkbox-1']")
    HOBBIES_2 = (By.XPATH, "//input[@id='hobbies-checkbox-2']")
    HOBBIES_3 = (By.XPATH, "//input[@id='hobbies-checkbox-3']")
    UPLOAD_PICTURES = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    STATE = (By.XPATH, "//div[@id='state']")
    ALL_STATES = (By.XPATH, "//div[@id='state']//child::div[@class=' css-1uccc91-singleValue']")
    CITY = (By.XPATH, "//div[@id='city']")

    SUBMIT = (By.XPATH, "//button[@id='submit']")

    def fill_text_fields(self):
        faker = Faker()
        first_name = faker.name()
        self.driver.find_element(*StudentPage.FIRST_NAME).send_keys(first_name)

        last_name = faker.name()
        self.driver.find_element(*StudentPage.LAST_NAME).send_keys(last_name)

        email = faker.email()
        self.driver.find_element(*StudentPage.EMAIL).send_keys(email)

        mobile = fake_phone_number(faker)
        self.driver.find_element(*StudentPage.MOBILE).send_keys(mobile)

        # subject = fake.word()
        # self.driver.find_element(*StudentPage.EMAIL).send_keys(email)
        # + нажать enter

        current_address = faker.address()
        self.driver.find_element(*StudentPage.CURRENT_ADDRESS).send_keys(current_address)

    def click_random_gender_radio_button(self):
        action = ActionChains(self.driver)  # todo КАК СДЕЛАТЬ ОДНУ ПЕРЕДАЧУ ACTIONS
        gender_list = self.driver.find_elements(*StudentPage.ALL_GENDER_RADIO)
        random_gender = gender_list[random.randint(0, len(gender_list) - 1)]
        action.move_to_element(random_gender).click(random_gender).perform()

    def click_random_month_date_of_birth(self):
        date_of_birth = self.driver.find_element(*StudentPage.DATE_OF_BIRTH)
        date_of_birth.click()
        all_months_list = self.driver.find_elements(*StudentPage.ALL_MONTHS_DATE_OF_BIRTH)
        all_years_list = self.driver.find_elements(*StudentPage.ALL_YEAR_DATE_OF_BIRTH)
        click_month = self.driver.find_element(*StudentPage.CLICK_MONTH)
        click_year = self.driver.find_element(*StudentPage.CLICK_YEAR)

        random_month = all_months_list[random.randint(0, len(all_months_list) - 1)]
        random_year = all_years_list[random.randint(0, len(all_years_list) - 1)]

        click_month.click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(random_month)).click()

        click_year.click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(random_year)).click()

        action = ActionChains(self.driver)  # todo КАК СДЕЛАТЬ ОДНУ ПЕРЕДАЧУ ACTIONS
        action.send_keys(Keys.ESCAPE).perform()

    def click_random_hobby(self):
        hobbies_list = self.driver.find_elements(*StudentPage.ALL_HOBBIES)
        random_hobby = hobbies_list[random.randint(0, len(hobbies_list) - 1)]
        action = ActionChains(self.driver)  # todo КАК СДЕЛАТЬ ОДНУ ПЕРЕДАЧУ ACTIONS
        action.move_to_element(random_hobby).click(random_hobby).perform()

    def choose_picture(self):
        return self.driver.find_element(*StudentPage.UPLOAD_PICTURES)

    def click_random_state(self):
        state = self.driver.find_element(*StudentPage.STATE)
        BasePage.scroll_down(self, state)
        action = ActionChains(self.driver)  # todo КАК СДЕЛАТЬ ОДНУ ПЕРЕДАЧУ ACTIONS
        action.move_to_element(state).double_click(state).perform()
        all_states = self.driver.find_element(*StudentPage.ALL_STATES)
        random_state = all_states[random.randint(0, len(all_states) - 1)]
        action.move_to_element(random_state).click(random_state).perform()

    def click_submit_button(self):
        return self.driver.find_element(*StudentPage.SUBMIT)

    # ActionChains(self.driver).click(first_name).send_keys("WoW").perform()
    # first_name = self.driver.find_element(StudentPage.FIRST_NAME)


from config import PROJECT_PATH

from utilities.utulities import *
