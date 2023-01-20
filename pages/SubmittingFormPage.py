from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SubmittingFormPage(BasePage):
    VALUES_NAME = (By.XPATH, f"//*[@class='table table-dark table-striped table-bordered table-hover']//*[contains("
                             "text(),'{value_name}')]")
