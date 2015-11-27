from basetestcase import BaseTestCase
from pages.home import Home
import unittest

class HomeTest(BaseTestCase):
    def test_logo_link_destination_is_correct(self):
        home = Home(self.driver)
        home.open()
        home._validate_page(self.driver)
        link = Home.Header._logo_url
        url = home.link_destination(link.get('locator'))
        self.assertTrue(url.endswith(link.get('suffix')), '%s does not ends with %s' %(url, link.get('suffix')))

    def test_nav_links_destinations_are_correct(self):
        home = Home(self.driver)
        home.open()
        home._validate_page(self.driver)
        bad_links = []
        for link in Home.Header.nav_links_list:
            url = home.link_destination(link.get('locator'))
            if not url.endswith(link.get('suffix')):
                bad_links.append((url))
        self.assertEqual(0, len(bad_links), 'there are %s bad links: '%(len(bad_links))+', '.join(bad_links))

    def test_login_link_destination_is_correct(self):
        home = Home(self.driver)
        home.open()
        home._validate_page(self.driver)
        link = Home.Header.login
        url = home.link_destination(link.get('locator'))
        self.assertTrue(url.endswith(link.get('suffix')), '%s is bad'%(url))

    def test_sign_up_link_destination_is_correct(self):
        home = Home(self.driver)
        home.open()
        home._validate_page(self.driver)
        link = Home.Header.sign_up
        url = home.link_destination(link.get('locator'))
        self.assertTrue(url.endswith(link.get('suffix')), '%s is bad'%(url))

    def test_nav_links_text_is_correct(self):
        home = Home(self.driver)
        home.open()
        home._validate_page(self.driver)
        bad_links = []
        home.click_filtr_btn(Home.Header.filtr_button['locator'])
        for link in Home.Header.nav_links_list:
            text = home.link_text(link.get('locator'))
            if text != link.get('text'):
                bad_links.append('%s links %s'%(text, link.get('suffix')))
        self.assertEqual(0, len(bad_links), 'there are %s invalid links: '%(len(bad_links))+', '.join(bad_links))

class HomeAddedLinkTest(BaseTestCase):
    def test_ordinal_number_is_correct(self):
        home = Home(self.driver)
        home.open()
        self.assertEqual(home.lp.get('text'), home.link_lp(), 'expected ordinal number to be: %s, found %s instead'%(home.lp.get('text'), home.link_lp()))

    def test_link_title_part_one_is_correct(self):
        home = Home(self.driver)
        home.open()
        self.assertEqual(home.link_title_part_one.get('text'), home.link_title_one(), 'expected link title part one to be: %s, found %s instead'%(home.link_title_part_one.get('text'), home.link_title_one()))

    def test_link_title_part_two_is_correct(self):
        home = Home(self.driver)
        home.open()
        self.assertEqual(home.link_title_part_two.get('text'), home.link_title_two(), 'expected link title part one to be: %s, found %s instead'%(home.link_title_part_two.get('text'), home.link_title_two()))

    def test_link_img_is_present(self):
        home = Home(self.driver)
        home.open()
        self.assertTrue(home.is_link_img_visible(), 'exptected link img to be visible but didnt found the img')

    def test_link_tag_is_correct(self):
        home = Home(self.driver)
        home.open()
        self.assertEqual(home.link_tags.get('text'), home.link_tag(), 'expected tag to be: %s found %s instead'%(home.link_tags.get('text'),home.link_tag()))

    def test_link_comment_is_correct(self):
        home = Home(self.driver)
        home.open()
        self.assertEqual(home.link_comments.get('text'), home.link_comment(), 'expected comment to be: %s found %s instead'%(home.link_comments.get('text'), home.link_comment()))