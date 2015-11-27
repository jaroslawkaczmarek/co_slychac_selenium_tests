from basetestcase import BaseTestCase
from pages.add_new_link import AddNewLink

class AddNewLinkTest(BaseTestCase):
    def test_add_new_link(self):
        link = AddNewLink(self.driver)
        link.open()
        link._validate_page(self.driver)
        link.url_input('http://wp.pl')
        link.title_input('wp test')
        link.tag_input('wroclaw')
        link.start_date_input()
        link.submit_form()
        link.wait_for_success_msg()
        current_url = self.driver.current_url
        self.assertTrue(link._add_new_link_url==current_url, 'expected current url to be: %s found %s instead'%(link._add_new_link_url, current_url))