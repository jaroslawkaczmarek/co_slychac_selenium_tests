from basetestcase import BaseTestCase
from pages.login import Login
from pages.home import Home
import unittest

class LoginTest(BaseTestCase):

    def test_login_user(self):
        login = Login(self.driver)
        login.open()
        login._validate_page(self.driver)
        login.username_input('test')
        login.password_input('test')
        login.submit_form()
        login.wait_for_logout_btn()
        current_url = self.driver.current_url
        self.assertTrue(Home._home_url==current_url, 'expected current url to be: %s found %s instead'%(Home._home_url, current_url))

    def test_wrong_credentials_msg(self):
        login = Login(self.driver)
        login.open()
        login._validate_page(self.driver)
        login.username_input('test333')
        login.password_input('test333')
        login.submit_form()
        login.wait_for_wrong_credentials_msg()
        current_url = self.driver.current_url
        self.assertTrue(login._login_url==current_url, 'expected current url to be: %s found %s instead'%(Home._home_url, current_url))