from base import Base, InvalidPageException
from home import Home
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddNewLink(Base):
    _add_new_link_url = Base.base_url + '/dodaj'
    _add_new_link_title = 'Dodaj nowy link'

    success_msg = {'locator':(By.ID, 'successAlert')}

    url = {'locator':(By.ID, 'new_link')}
    title = {'locator':(By.ID, 'url_title')}
    tag = {'locator':(By.ID, 'links_tag')}
    start_date = {'locator':(By.ID, 'start')}
    set_start_date = {'locator':(By.CSS_SELECTOR, '.table-condensed tbody > tr:nth-of-type(3) > td')}
    input_date_today = {'locator':(By.CSS_SELECTOR, '.table-condensed tfoot > tr > th.today')}
    end_date = {'locator':(By.ID, 'end')}

    send_btn = {'locator':(By.CSS_SELECTOR, '.col-sm-6 > input.btn-primary')}

    def _validate_page(self, driver):
        if not driver.title == self._add_new_link_title:
            raise InvalidPageException
        return True

    def open(self):
        home = Home(self.driver)
        home.open()
        home.click_login_btn()
        login = Login(self.driver)
        login.login_user()
        self.go_to_page(self._add_new_link_url)

    def url_input(self, url):
        self.driver.find_element(*self.url.get('locator')).send_keys(url)

    def title_input(self, title):
        self.driver.find_element(*self.title.get('locator')).send_keys(title)

    def tag_input(self, tag):
        tag_field = self.driver.find_element(*self.tag.get('locator'))
        tag_field.clear()
        tag_field.send_keys(tag)
        tag_field.send_keys(Keys.ENTER)

    def start_date_input(self):
        date = self.driver.find_element(*self.start_date.get('locator'))
        date.click()
        self.wait_for_element(self.input_date_today.get('locator'))
        self.driver.find_element(*self.input_date_today.get('locator')).click()
        '''self.wait_for_element(self.set_start_date.get('locator'))
        self.driver.find_element(*self.set_start_date.get('locator')).click()'''
        date.send_keys(Keys.ESCAPE)

    def end_date_input(self, end_date):
        pass

    def submit_form(self):
        self.driver.find_element(*self.send_btn.get('locator')).click()

    def wait_for_success_msg(self):
        self.wait_for_element(self.success_msg.get('locator'))

