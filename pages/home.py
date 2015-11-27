from base import Base, InvalidPageException
from selenium.webdriver.common.by import By

class Home(Base):
    _home_title = 'Home Page'
    _home_url = Base.base_url + '/'

    lp = {'locator':(By.CSS_SELECTOR, '.lp'),
          'text':'1'}
    link_title_part_one = {'locator': (By.CSS_SELECTOR, 'p.title a.title'),
                           'text': 'wp test'}
    link_title_part_two = {'locator': (By.CSS_SELECTOR, 'p.title span.source > small'),
                           'text': '//wp.pl'}
    link_pic = {'locator': (By.CSS_SELECTOR, '#post_visibility > a.pic > img')}
    link_author = {'locator':(By.CSS_SELECTOR, 'p.author a.author'),
                   'text': 'jarek'}
    link_tags = {'locator': (By.CSS_SELECTOR, 'p.tags > a > span'),
                'text': 'wroclaw'}
    link_comments = {'locator': (By.CSS_SELECTOR, 'ul.flat-list > li >a'),
                     'text': '0 komentarzy'}
    link_likes = {'locator': (By.CSS_SELECTOR, 'li#star span.rank'),
                  'text': '0'}
    link_hide = {'locator': (By.CSS_SELECTOR, 'li#zakryj > .zakryj'),
                 'text': 'zakryj'}

    def _validate_page(self, driver):
        if not driver.title == self._home_title:
            raise InvalidPageException

    def open(self):
        self.go_to_page(self._home_url)

    def click_filtr_btn(self, locator):
        btn = self.driver.find_element(*locator)
        btn.click()

    def click_login_btn(self):
        self.click_element(Home.Header.login.get('locator'))

    def link_lp(self):
        return self.driver.find_element(*self.lp.get('locator')).text

    def link_title_one(self):
        return self.driver.find_element(*self.link_title_part_one.get('locator')).text

    def link_title_two(self):
        return self.driver.find_element(*self.link_title_part_two.get('locator')).text

    def is_link_img_visible(self):
        return self.driver.find_element(*self.link_pic.get('locator')).is_displayed()

    def link_tag(self):
        return self.driver.find_element(*self.link_tags.get('locator')).text

    def link_comment(self):
        return self.driver.find_element(*self.link_comments.get('locator')).text

    def is_link_like_visible(self):
        return self.driver.find_element(*self.link_likes.get('locator')).is_displayed()

    def link_like(self):
        return self.driver.find_element(*self.link_likes.get('locator')).text

    def is_link_hide_link_visible(self):
        return self.driver.find_element(*self.link_hide.get('locator')).is_displayed()

    def link_hide_link(self):
        return self.driver.find_element(*self.link_hide.get('locator')).text
