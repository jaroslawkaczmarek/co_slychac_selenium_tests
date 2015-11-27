from base import Base, InvalidPageException
from selenium.webdriver.common.by import By
from pages.home import Home

class SignUp(Base):
    _sign_up_url = Base.base_url + '/rejestracja/'
    _sign_up_title = 'Rejestracja'

    user_name_exists_already_msg = {'locator':(By.CSS_SELECTOR, 'p.text-danger')}

    user_name = {'locator': (By.NAME, 'username')}
    password = {'locator': (By.NAME, 'password')}
    email = {'locator': (By.NAME, 'email')}
    sign_up_btn = {'locator': (By.CSS_SELECTOR,'.col-sm-offset-2 > button')}

    def open(self):
        self.go_to_page(self._sign_up_url)

    def _validate_page(self, driver):
        if not driver.title == self._sign_up_title:
            raise InvalidPageException

    def username_input(self, username):
        self.driver.find_element(*self.user_name.get('locator')).send_keys(username)

    def password_input(self, password):
        self.driver.find_element(*self.password.get('locator')).send_keys(password)

    def email_input(self, email):
        self.driver.find_element(*self.email.get('locator')).send_keys(email)

    def submit_form(self):
        self.driver.find_element(*self.sign_up_btn.get('locator')).click()

    def wait_for_logout_btn(self):
        self.wait_for_element(Home.Header.logout.get('locator'))

    def wait_for_user_already_exists_msg(self):
        self.wait_for_element(self.user_name_exists_already_msg.get('locator'))


