from faker import Faker


def fake_phone_number(fake: Faker) -> str:
    return f'+7 {fake.msisdn()[1:]}'
