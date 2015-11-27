from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import abstractmethod
import requests
from requests import Timeout

class Base(object):
    base_url = "http://localhost:5000"
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def link_destination(self, locator):
        link = self.driver.find_element(*locator)
        return link.get_attribute('href')

    def link_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @abstractmethod
    def _validate_page(self, driver):
        pass

    def click_element(self, locator):
        self.driver.find_element(*locator).click()


    class Header(object):
        _logo_url = {'locator':(By.ID, 'brand-overrides'),
                     'suffix':'/'}
        filtr_button = {'locator':(By.CSS_SELECTOR, 'li#filtr > a')}
        nav_links_list = [
            {'locator':(By.CSS_SELECTOR, 'li#filtr ul.dropdown-menu > li:nth-of-type(1) > a'),
             'suffix':'/dzis',
             'text':'Dzis'},
            {'locator':(By.CSS_SELECTOR, 'li#filtr ul.dropdown-menu > li:nth-of-type(2) > a'),
             'suffix':'/jutro',
             'text':'Jutro'},
            {'locator':(By.CSS_SELECTOR, 'li#filtr ul.dropdown-menu > li:nth-of-type(3) > a'),
             'suffix':'/tydzien',
             'text':'Tydzien'},
            {'locator':(By.CSS_SELECTOR, 'li#filtr ul.dropdown-menu > li:nth-of-type(4) > a'),
             'suffix':'/miesiac',
             'text':'Miesiac'},
        ]
        search_input = {'locator': (By.ID, 'searchInput')}
        search_button = {'locator':(By.CSS_SELECTOR, 'form.pull-left button')}

        login = {'locator':(By.CSS_SELECTOR, 'ul.pull-right > li:nth-of-type(1) > a'),
                 'suffix': '/login'}
        sign_up = {'locator':(By.CSS_SELECTOR, 'ul.pull-right > li:nth-of-type(2) > a'),
                   'suffix': '/rejestracja/'}

        logout = {'locator':(By.LINK_TEXT, 'Wyloguj')}
        add_new_link_btn = {'locator':(By.LINK_TEXT, 'Dodaj link')}

    class Footer(object):
        footer_link = {'locator': (By.CSS_SELECTOR, '#footer .pull-right > p:nth-of-type(2) > a')}

class InvalidPageException(Exception):
    pass