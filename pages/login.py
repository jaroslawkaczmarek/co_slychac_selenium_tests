from base import Base, InvalidPageException
from pages.home import Home
from selenium.webdriver.common.by import By

class Login(Base):
    _login_url = Base.base_url + '/login'
    _login_title = 'Logowanie'

    wrong_credentials_msg = {'locator':(By.CSS_SELECTOR, 'p.text-danger')}

    user_name = {'locator': (By.NAME, 'username')}
    password = {'locator': (By.NAME, 'password')}
    login_btn = {'locator':(By.CSS_SELECTOR, '.col-sm-offset-2 > button')}

    def open(self):
        self.go_to_page(self._login_url)

    def _validate_page(self, driver):
        if not driver.title == self._login_title:
            raise InvalidPageException

    def username_input(self, username):
        self.driver.find_element(*self.user_name.get('locator')).send_keys(username)

    def password_input(self, password):
        self.driver.find_element(*self.password.get('locator')).send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.login_btn.get('locator')).click()

    def wait_for_logout_btn(self):
        self.wait_for_element(Home.Header.logout.get('locator'))

    def wait_for_wrong_credentials_msg(self):
        self.wait_for_element(self.wrong_credentials_msg.get('locator'))

    def login_user(self):
        self.open()
        self._validate_page(self.driver)
        self.username_input('test')
        self.password_input('test')
        self.submit_form()
        self.wait_for_logout_btn()
