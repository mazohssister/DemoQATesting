from faker import Faker
from datas.data import Student
from utilities import utilities

faker = Faker()


def student_info_generator():
    yield Student(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        mobile=utilities.random_phone_number(),
        current_address=faker.city()
    )
