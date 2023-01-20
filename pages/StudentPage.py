from selenium.webdriver.common.by import By
from datas.data_generator import student_info_generator
from pages.BasePage import BasePage
from utilities.utilities import *


class StudentPage(BasePage):
    FIRST_NAME_FIELD = (By.XPATH, "//*[@id='firstName']")
    LAST_NAME_FIELD = (By.XPATH, "//*[@id='lastName']")
    EMAIL_FIELD = (By.XPATH, "//*[@id='userEmail']")
    GENDER_BUTTON_MALE = (By.XPATH, "//*[@id='gender-radio-1']")
    GENDER_BUTTON_FEMALE = (By.XPATH, "//*[@id='gender-radio-2']")
    GENDER_BUTTON_OTHER = (By.XPATH, "//*[@id='gender-radio-3']")
    GENDER_BUTTON_OPTIONS = (By.XPATH, "//*[@class='col-md-9 col-sm-12']//*[contains(@for, 'gender-radio')]")
    MOBILE_FIELD = (By.XPATH, "//*[@id='userNumber']")
    DATE_OF_BIRTH_CALENDAR = (By.XPATH, "//*[@id='dateOfBirthInput']")
    YEAR_DROPDOWN = (By.XPATH, "//*[@class='react-datepicker__year-select']")
    YEAR_DROPDOWN_OPTIONS = (By.XPATH, "//*[@class='react-datepicker__year-select']/option")
    MONTH_DROPDOWN = (By.XPATH, "//*[@class='react-datepicker__month-select']")
    MONTH_DROPDOWN_OPTIONS = (By.XPATH, "//*[@class='react-datepicker__month-select']//option")
    DAY_OPTIONS = (
        By.XPATH, "//div[ @class ='react-datepicker__month']//*[@ class ""='react-datepicker__week']//child::*")
    SUBJECTS_INPUT = (By.XPATH, "//*[@id='subjectsInput']")
    SUBJECTS_OPTIONS = (By.XPATH, "//*[contains(@id, 'react-select-2-option')]")
    HOBBIES_OPTIONS = (By.XPATH, "//*[@class='col-md-9 col-sm-12']//*[contains(@for, 'hobbies-checkbox')]")
    HOBBIES_CHECKBOX_1 = (By.XPATH, "//*[@id='hobbies-checkbox-1']")
    HOBBIES_CHECKBOX_2 = (By.XPATH, "//*[@id='hobbies-checkbox-2']")
    HOBBIES_CHECKBOX_3 = (By.XPATH, "//*[@id='hobbies-checkbox-3']")
    UPLOAD_PICTURES = (By.XPATH, "//*[@id='uploadPicture']")
    CURRENT_ADDRESS_FIELD = (By.XPATH, "//*[@id='currentAddress']")
    STATE_DROPDOWN = (By.XPATH, "//*[@id='state']")
    STATE_DROPDOWN_OPTIONS = (By.XPATH, "//*[contains(@id, 'react-select-3-option')]")
    CITY_DROPDOWN = (By.XPATH, "//*[@id='city']")
    CITY_DROPDOWN_OPTIONS = (By.XPATH, "//*[contains(@id, 'react-select-4-option')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

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
        student_info = next(student_info_generator())

        full_name = f'{student_info.first_name} {student_info.last_name}'
        first_name = student_info.first_name
        last_name = student_info.last_name
        email = student_info.email
        mobile = student_info.mobile
        current_address = student_info.current_address

        self.driver.find_element(*StudentPage.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*StudentPage.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*StudentPage.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*StudentPage.MOBILE_FIELD).send_keys(mobile)
        self.driver.find_element(*StudentPage.CURRENT_ADDRESS_FIELD).send_keys(current_address)

        return full_name, email, mobile, current_address

    def output_text_fields(self):
        full_name = self.driver.find_element(*StudentPage.OUTPUT_FULL_NAME).text
        email = self.driver.find_element(*StudentPage.OUTPUT_EMAIL).text
        mobile = self.driver.find_element(*StudentPage.OUTPUT_MOBILE).text
        current_address = self.driver.find_element(*StudentPage.OUTPUT_CURRENT_ADDRESS).text
        return full_name, email, mobile, current_address

    def click_random_gender_radio_button(self):
        gender_list = self.driver.find_elements(*StudentPage.GENDER_BUTTON_OPTIONS)
        gender = BasePage.choose_random_element(self, gender_list)
        BasePage.action_move_to_element_click(self, gender)
        return gender.text

    def check_output_gender(self):
        return self.driver.find_element(*StudentPage.OUTPUT_GENDER).text

    def click_random_month_year_day_date_of_birth(self):
        self.driver.find_element(*StudentPage.DATE_OF_BIRTH_CALENDAR).click()
        self.driver.find_element(*StudentPage.MONTH_DROPDOWN).click()
        month_list = self.driver.find_elements(*StudentPage.MONTH_DROPDOWN_OPTIONS)
        random_month = self.choose_random_element(month_list)
        random_month_text = random_month.text
        random_month.click()

        self.driver.find_element(*StudentPage.YEAR_DROPDOWN).click()
        year_list = self.driver.find_elements(*StudentPage.YEAR_DROPDOWN_OPTIONS)
        random_year = self.choose_random_element(year_list)
        random_year.click()
        random_year_text = random_year.text

        day_list = self.driver.find_elements(*StudentPage.DAY_OPTIONS)
        random_day = self.choose_random_element(day_list)
        random_day_text = random_day.text
        random_day_text = BasePage.zero_before_day(self, random_day_text)
        random_day.click()

        return f'{random_day_text} {random_month_text},{random_year_text}'

    def check_output_date_of_birth(self):
        return self.driver.find_element(*StudentPage.OUTPUT_DATE_OF_BIRTH).text

    def choose_random_subject(self):
        letter_list = 'ertyuiopasdghlcvbnm'
        rand_letters = random.choice(letter_list)

        subject = self.driver.find_element(*StudentPage.SUBJECTS_INPUT)
        subject.click()
        subject.send_keys(rand_letters)
        subject_list = self.driver.find_elements(*StudentPage.SUBJECTS_OPTIONS)
        subject_list_text = subject_list[0].text
        self.action_move_to_element_click(subject_list[0])

        return subject_list_text

    def check_output_subject(self):
        return self.driver.find_element(*StudentPage.OUTPUT_SUBJECT).text

    def click_random_hobby(self):
        hobbies_list = self.driver.find_elements(*StudentPage.HOBBIES_OPTIONS)
        random_hobby = self.choose_random_element(hobbies_list)
        self.action_move_to_element_click(random_hobby)
        return random_hobby.text

    def check_output_hobbies(self):
        return self.driver.find_element(*StudentPage.OUTPUT_HOBBIES).text

    def choose_picture(self):
        return self.driver.find_element(*StudentPage.UPLOAD_PICTURES)

    def click_random_state_city(self):
        self.driver.set_window_size(670, 847)

        state = self.driver.find_element(*StudentPage.STATE_DROPDOWN)
        self.scroll_down(state)
        self.action_move_to_element_click(state)

        state_list = self.driver.find_elements(*StudentPage.STATE_DROPDOWN_OPTIONS)
        random_state = self.choose_random_element(state_list)
        state_text = random_state.text
        self.action_move_to_element_click(random_state)

        city = self.driver.find_element(*StudentPage.CITY_DROPDOWN)
        self.go_to_element(city)
        self.action_move_to_element_click(city)

        city_list = self.driver.find_elements(*StudentPage.CITY_DROPDOWN_OPTIONS)
        random_city = self.choose_random_element(city_list)
        city_text = random_city.text
        self.action_move_to_element_click(random_city)

        return f'{state_text} {city_text}'

    def check_output_state_city(self):
        return self.driver.find_element(*StudentPage.OUTPUT_STATE_CITY).text

    def click_submit_button(self):
        submit = self.driver.find_element(*StudentPage.SUBMIT_BUTTON)
        self.action_move_to_element_click(submit)
