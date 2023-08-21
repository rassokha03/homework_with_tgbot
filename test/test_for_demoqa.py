import datetime
import allure

from demoqa.pages.registration_page import RegistrationPage
from demoqa.models.users import User

@allure.title('Successful fill form')
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


    with allure.step("Open registration page"):
        registration_page.open()
    with allure.step("Fill registration form"):
        registration_page.register(andrey)
    with allure.step("Assert registered and registration info correct"):
        registration_page.should_have_registered(andrey)