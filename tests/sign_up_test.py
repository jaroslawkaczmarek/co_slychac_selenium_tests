import unittest
from pages.sign_up import SignUp
from basetestcase import BaseTestCase
from pages.home import Home

class SignupTest(BaseTestCase):
    def test_signup_form(self):
        signup = SignUp(self.driver)
        signup.open()
        signup._validate_page(self.driver)
        signup.username_input('test')
        signup.password_input('test')
        signup.email_input('test@gmail.com')
        signup.submit_form()
        signup.wait_for_logout_btn()
        current_url = self.driver.current_url
        self.assertTrue(current_url==Home._home_url, 'expected current url to be: %s found %s instead'%(Home._home_url, current_url))

    def test_user_exists_already_msg(self):
        signup = SignUp(self.driver)
        signup.open()
        signup._validate_page(self.driver)
        signup.username_input('test')
        signup.password_input('test')
        signup.email_input('test@gmail.com')
        signup.submit_form()
        signup.wait_for_user_already_exists_msg()
        current_url = self.driver.current_url
        self.assertTrue(current_url==signup._sign_up_url, 'expected url to be: %s found %s instead'%(signup._sign_up_url,current_url))
