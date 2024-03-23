import random
from pprint import pprint

from faker import Faker
from data import User

faker_en = Faker('En')
Faker.seed()

def generated_user(phone_len):
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        phone_number=generated_phone_number(phone_len)
    )


def generated_name():
    female = faker_en.name_female()
    male = faker_en.name_male()
    return random.choice([male, female])

def generated_phone_number(n):
    number_len = n - 4
    number = '+966' + ''.join([str(random.randint(0, 9))for _ in range(number_len)])
    return number

a = next(generated_user(30))
print(a)
print(a.first_name)
print(a.last_name)
