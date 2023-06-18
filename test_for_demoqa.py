import os.path

from selene import browser, have

def test_form():
    browser.open('/')

    #Filling out the form

    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('first@mail.com')
    browser.element('//label[contains(text(), "Male")]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1995"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="4"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').type('Civics').press_enter()
    browser.element('//label[contains(text(), "Sports")]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('picture/cat.jpg'))
    browser.element('#currentAddress').type('Санкт-Петербург')
    browser.element('#state').click()
    browser.element('//*[.="Haryana"]').click()
    browser.element('#city').click()
    browser.element('//*[.="Karnal"]').click()
    browser.element('#submit').press_enter()

    #Tests

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Иван Иванов'))
    browser.element('.table-responsive').should(have.text('first@mail.com'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('1234567890'))
    browser.element('.table-responsive').should(have.text('31 May,1995'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('cat.jpg'))
    browser.element('.table-responsive').should(have.text('Санкт-Петербург'))
    browser.element('.table-responsive').should(have.text('Haryana Karnal'))
    browser.element('#closeLargeModal').click()









