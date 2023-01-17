import os

import pytest

from config import PROJECT_PATH
from pages.StudentPage import StudentPage


@pytest.mark.usefixtures("setup")
class Test:
    def test_main(self):
        sp_test = StudentPage(self.driver)
        sp_test.fill_text_fields()
        sp_test.click_random_gender_radio_button()
        sp_test.click_random_month_date_of_birth()
        sp_test.click_random_hobby()
        sp_test.choose_picture().send_keys(os.path.join(PROJECT_PATH, "datas\\igK4HwxAGqY.jpg"))
        # sp_test.click_random_state()
