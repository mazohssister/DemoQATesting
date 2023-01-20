import os
import pytest
from config import PROJECT_PATH
from pages.StudentPage import StudentPage


@pytest.mark.usefixtures("setup")
class Test:
    def test_main(self):
        sp_test = StudentPage(self.driver)
        input_full_name, input_email, input_mobile, input_current_address = sp_test.fill_text_fields()

        input_gender = sp_test.click_random_gender_radio_button()
        input_date_of_birth = sp_test.click_random_month_year_day_date_of_birth()
        input_subject = sp_test.choose_random_subject()
        input_hobbies = sp_test.click_random_hobby()
        sp_test.choose_picture().send_keys(os.path.join(PROJECT_PATH, "datas\\igK4HwxAGqY.jpg"))
        input_state_city = sp_test.click_random_state_city()
        sp_test.click_submit_button()

        output_full_name, output_email, output_mobile, output_current_address = sp_test.output_text_fields()
        assert input_full_name == output_full_name, "the full name does not match"
        assert input_email == output_email, "the email does not match"
        assert input_mobile == output_mobile, "the mobile does not match"
        assert input_current_address == output_current_address, "the current address does not match"

        output_gender = sp_test.check_output_gender()
        assert input_gender == output_gender, "gender doesnt match"

        output_date_of_birth = sp_test.check_output_date_of_birth()
        assert input_date_of_birth == output_date_of_birth, "date of birth doesnt match"

        output_subject = sp_test.check_output_subject()
        assert input_subject == output_subject, "subjects doesnt match"

        output_hobbies = sp_test.check_output_hobbies()
        assert input_hobbies == output_hobbies, "hobbies doesnt match"

        output_state_city = sp_test.check_output_state_city()
        assert input_state_city == output_state_city, "subjects doesnt match"
