from selenium.webdriver.support.select import Select
from models.user import User


class UserHelper:

    def __init__(self, app):
        self.app = app

    def jump_to_add_new_user_form(self):
        wd = self.app.wd
        # click new user button
        wd.find_element_by_link_text("add new").click()

    def create_new_user(self):
        wd = self.app.wd
        # submit user form
        wd.find_element_by_name("submit").click()

    def jump_to_edit_first_user_form(self):
        wd = self.app.wd
        # click edit first user button
        wd.find_element_by_xpath("//td[8]/a").click()

    def update_user(self):
        wd = self.app.wd
        # submit user form
        wd.find_element_by_xpath("//input[22]").click()

    def fill_user_form(self, user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.fname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.mname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.lname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(user.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(user.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(
            "January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(user.note)

    def delete_user(self):
        wd = self.app.wd
        # submit deletion
        wd.find_element_by_xpath("//form[2]/input[2]").click()

    def user_count(self):
        wd = self.app.wd
        self.app.go_to_home()
        return len(wd.find_elements_by_xpath("//td[8]/a"))

    def get_user_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[1]/a").click()
        user_list = []
        for element in wd.find_elements_by_xpath("//tr/td/input"):
            id = element.get_attribute("id")
            fname = element.get_attribute("title").split()[1][1:]
            lname = element.get_attribute("title").split()[2][:-1]
            user_list.append(User(fname=fname, lname=lname, id=id))
        return user_list
