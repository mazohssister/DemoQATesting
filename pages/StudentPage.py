from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.BasePage import BasePage
from utilities.utulities import *


class StudentPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER_RADIO_MALE = (By.XPATH, "//input[@id='gender-radio-1']")
    GENDER_RADIO_FEMALE = (By.XPATH, "//input[@id='gender-radio-2']")
    GENDER_RADIO_OTHER = (By.XPATH, "//input[@id='gender-radio-3']")
    ALL_GENDER_RADIO = (By.XPATH, "//*[@class='col-md-9 col-sm-12']//*[contains(@for, 'gender-radio')]")
    ALL_MONTHS_DATE_OF_BIRTH = (By.XPATH, "//select[@class='react-datepicker__month-select']/option")
    ALL_YEAR_DATE_OF_BIRTH = (By.XPATH, "//select[@class='react-datepicker__year-select']/option")
    CLICK_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    DATE_OF_BIRTH_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    SUBJECTS = (By.XPATH, "//*[@id='subjectsInput']")
    SUBJECTS_OPTIONS = (By.XPATH, "//*[contains(@id, 'react-select-2-option')]")
    ALL_HOBBIES = (By.XPATH, "//*[@class='col-md-9 col-sm-12']//*[contains(@for, 'hobbies-checkbox')]")
    HOBBIES_1 = (By.XPATH, "//*[@id='hobbies-checkbox-1']")
    HOBBIES_2 = (By.XPATH, "//*[@id='hobbies-checkbox-2']")
    HOBBIES_3 = (By.XPATH, "//*[@id='hobbies-checkbox-3']")
    UPLOAD_PICTURES = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    STATE = (By.XPATH, "//*[@id='state']")
    ALL_STATES = (By.XPATH, "//*[contains(@id, 'react-select-3-option')]")
    CITY = (By.XPATH, "//div[@id='city']")
    ALL_CITY = (By.XPATH, "//*[contains(@id, 'react-select-4-option')]")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    OUTPUT_FULL_NAME = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                                  "table-hover']//*[contains(text(), 'Student Name')]//following-sibling::*")
    OUTPUT_EMAIL = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                              "table-hover']//*[contains(text(), 'Student Email')]//following-sibling::*")
    OUTPUT_MOBILE = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                               "table-hover']//*[contains(text(), 'Mobile')]//following-sibling::*")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped "
                                        "table-bordered table-hover']//*[contains(text(), "
                                        "'Address')]//following-sibling::*")
    OUTPUT_GENDER = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                               "table-hover']//*[contains(text(), 'Gender')]//following-sibling::*")
    OUTPUT_DATE_OF_BIRTH = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped "
                                      "table-bordered table-hover']//*[contains(text(), 'Date of "
                                      "Birth')]//following-sibling::*")
    OUTPUT_SUBJECT = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                                "table-hover']//*[contains(text(), 'Subjects')]//following-sibling::*")
    OUTPUT_HOBBIES = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                                "table-hover']//*[contains(text(), 'Hobbies')]//following-sibling::*")
    OUTPUT_STATE_CITY = (By.XPATH, "//*[@class='modal-body']//*[@class='table table-dark table-striped table-bordered "
                                   "table-hover']//*[contains(text(), 'State and City')]//following-sibling::*")

    def fill_text_fields(self):
        faker = Faker()
        first_name = faker.first_name()
        self.driver.find_element(*StudentPage.FIRST_NAME).send_keys(first_name)

        last_name = faker.first_name()
        self.driver.find_element(*StudentPage.LAST_NAME).send_keys(last_name)

        email = faker.email()
        self.driver.find_element(*StudentPage.EMAIL).send_keys(email)

        mobile = random_phone_number()
        self.driver.find_element(*StudentPage.MOBILE).send_keys(mobile)

        current_address = faker.city()
        self.driver.find_element(*StudentPage.CURRENT_ADDRESS).send_keys(current_address)

        full_name = first_name + ' ' + last_name

        return full_name, email, mobile, current_address

    def output_text_fields(self):
        full_name = self.driver.find_element(*StudentPage.OUTPUT_FULL_NAME).text
        email = self.driver.find_element(*StudentPage.OUTPUT_EMAIL).text
        mobile = self.driver.find_element(*StudentPage.OUTPUT_MOBILE).text
        current_address = self.driver.find_element(*StudentPage.OUTPUT_CURRENT_ADDRESS).text
        return full_name, email, mobile, current_address

    def click_random_gender_radio_button(self):
        action = ActionChains(self.driver)
        gender_list = self.driver.find_elements(*StudentPage.ALL_GENDER_RADIO)
        gender = gender_list[random.randint(0, len(gender_list) - 1)]
        action.move_to_element(gender).click(gender).perform()
        return gender.text

    def check_output_gender(self):
        gender = self.driver.find_element(*StudentPage.OUTPUT_GENDER).text
        return gender

    def click_random_month_year_day_date_of_birth(self):
        self.driver.find_element(*StudentPage.DATE_OF_BIRTH).click()
        self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").click()
        month_list = self.driver.find_elements(By.XPATH, "//*[@class='react-datepicker__month-select']//option")
        random_month = month_list[random.randint(0, len(month_list) - 1)]
        random_month_text = random_month.text
        random_month.click()

        self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").click()
        year_list = self.driver.find_elements(By.XPATH, "//*[@class='react-datepicker__year-select']//option")
        random_year = year_list[random.randint(0, len(month_list) - 1)]
        random_year.click()
        random_year_text = random_year.text

        day_list = self.driver.find_elements(By.XPATH,
                                             "//div[ @class ='react-datepicker__month'] // *[@ class "
                                             "='react-datepicker__week'] // child::*")
        random_day = day_list[random.randint(6, len(day_list) - 14)]
        random_day_text = random_day.text
        random_day_text = BasePage.zero_before_day(self, random_day_text)
        random_day.click()

        date_of_birth = f'{random_day_text} {random_month_text},{random_year_text}'
        return date_of_birth

    def check_output_date_of_birth(self):
        date_of_birth = self.driver.find_element(*StudentPage.OUTPUT_DATE_OF_BIRTH).text
        return date_of_birth

    def choose_random_subject(self):
        action = ActionChains(self.driver)

        letter_list = 'ertyuiopasdghlcvbnm'
        rand_letters = random.choice(letter_list)

        subject = self.driver.find_element(*StudentPage.SUBJECTS)
        subject.click()
        subject.send_keys(rand_letters)
        subject_list = self.driver.find_elements(*StudentPage.SUBJECTS_OPTIONS)
        subject_list_text = subject_list[0].text
        action.move_to_element(subject_list[0])
        subject_list[0].click()

        return subject_list_text

    def check_output_subject(self):
        subject = self.driver.find_element(*StudentPage.OUTPUT_SUBJECT).text
        return subject

    def click_random_hobby(self):
        hobbies_list = self.driver.find_elements(*StudentPage.ALL_HOBBIES)
        random_hobby = hobbies_list[random.randint(0, len(hobbies_list) - 1)]
        action = ActionChains(self.driver)
        action.move_to_element(random_hobby).click(random_hobby).perform()
        return random_hobby.text

    def check_output_hobbies(self):
        return self.driver.find_element(*StudentPage.OUTPUT_HOBBIES).text

    def choose_picture(self):
        return self.driver.find_element(*StudentPage.UPLOAD_PICTURES)

    def click_random_state_city(self):
        action = ActionChains(self.driver)
        self.driver.set_window_size(670, 847)

        state = self.driver.find_element(*StudentPage.STATE)
        self.driver.execute_script("arguments[0].scrollIntoView();", state)
        action.move_to_element(state)
        state.click()

        state_list = self.driver.find_elements(*StudentPage.ALL_STATES)
        random_state = state_list[random.randint(0, len(state_list) - 1)]
        state_text = random_state.text
        action.move_to_element(random_state)
        random_state.click()

        city = self.driver.find_element(*StudentPage.CITY)
        self.driver.execute_script("arguments[0].scrollIntoView();", city)
        action.move_to_element(city)
        city.click()

        city_list = self.driver.find_elements(*StudentPage.ALL_CITY)
        random_city = city_list[random.randint(0, len(city_list) - 1)]
        city_text = random_city.text
        action.move_to_element(random_city)
        random_city.click()

        return f'{state_text} {city_text}'

    def check_output_state_city(self):
        return self.driver.find_element(*StudentPage.OUTPUT_STATE_CITY).text

    def click_submit_button(self):
        action = ActionChains(self.driver)
        submit = self.driver.find_element(*StudentPage.SUBMIT)
        action.move_to_element(submit)
        submit.click()
