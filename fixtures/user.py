from selenium.webdriver.support.select import Select
from models.user import User
import re


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
        self.user_cache = None

    def jump_to_edit_first_user_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[1]/a").click()
        wd.find_element_by_xpath("//tr[2]/td[8]/a").click()

    def jump_to_edit_user_form_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[1]/a").click()
        wd.find_elements_by_xpath("//td[8]/a")[index].click()

    def update_user(self):
        wd = self.app.wd
        # submit user form
        wd.find_element_by_xpath("//input[22]").click()
        self.user_cache = None

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
        wd.find_element_by_name("home").send_keys(user.home_phone)
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
        wd.find_element_by_name("email").send_keys(user.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(user.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(user.email3)
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
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(user.second_phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(user.note)

    def delete_user(self):
        wd = self.app.wd
        # submit deletion
        wd.find_element_by_xpath("//form[2]/input[2]").click()
        self.user_cache = None

    def user_count(self):
        wd = self.app.wd
        self.app.go_to_home()
        return len(wd.find_elements_by_xpath("//td[8]/a"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            wd.find_element_by_xpath("//li[1]/a").click()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.user_cache.append(User(id=id, fname=cells[2].text, lname=cells[1].text, address=cells[3].text,
                                            all_emails_from_home_page=cells[4].text, all_phones_from_home_page=cells[5].text))
        return list(self.user_cache)

    def jump_to_view_user_form_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[1]/a").click()
        wd.find_elements_by_xpath("//td[7]/a")[index].click()

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.jump_to_edit_user_form_by_index(index)
        fname = wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        second_phone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return User(fname=fname, lname=lname, id=id, home_phone=home_phone, mobile=mobile,
                    work_phone=work_phone, second_phone=second_phone, address=address, email1=email1,
                    email2=email2, email3=email3)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.jump_to_view_user_form_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        second_phone = re.search("P: (.*)", text).group(1)
        return User(home_phone=home_phone, mobile=mobile, work_phone=work_phone, second_phone=second_phone)
