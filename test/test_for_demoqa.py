from selene import have
from demoqa.pages.registration_page import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()

    (
        registration_page
        .fill_first_name('Иван')
        .fill_last_name('Иванов')
        .fill_email('first@mail.com')
        .fill_gender('Male')
        .fill_number('1234567890')
        .fill_date('1995', 'May', '31')
        .fill_subjects('Civics')
        .fill_hobbies('Sports')
        .fill_picture('cat.jpg')
        .fill_adress('Санкт-Петербург')
        .fill_state('Haryana')
        .fill_city('Karnal')
        .submit_form()
    )

    registration_page.should_have_text('Thanks for submitting the form')
    registration_page.registered_user_data.should(
        have.texts(
            'Иван Иванов',
            'first@mail.com',
            'Male',
            '1234567890',
            '31 May,1995',
            'Civics',
            'Sports',
            'cat.jpg',
            'Санкт-Петербург',
            'Haryana Karnal'
        )
    )

    registration_page.close()

    registration_page.should_be_clean()








