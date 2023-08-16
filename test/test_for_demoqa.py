import datetime

from demoqa.pages.registration_page import RegistrationPage
from demoqa.models.users import User


def test_form():
    registration_page = RegistrationPage()

    andrey = User(
        first_name='Иван',
        last_name='Иванов',
        email='first@mail.com',
        gender='Male',
        phone='1234567890',
        birthday=datetime.date(1995, 5, 31),
        hobby='Sports',
        subjects='Civics',
        image='cat.jpg',
        address='Санкт-Петербург',
        state='Haryana',
        city='Karnal'

    )
    registration_page.open()
    registration_page.register(andrey)
    registration_page.should_have_registered(andrey)