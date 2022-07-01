from random import choice
from string import ascii_letters, digits

from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper
from fixtures.user import UserHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def gen_random_string(self):
        r_str = ''.join(choice(ascii_letters) for i in range(5))
        return r_str

    def gen_random_number(self):
        r_mob = '+7' + ''.join(choice(digits) for i in range(10))
        return r_mob

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
