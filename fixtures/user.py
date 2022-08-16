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
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        wd.find_element_by_xpath("//tr[2]/td[8]/a").click()

    def jump_to_edit_user_form_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        wd.find_elements_by_xpath("//td[8]/a")[index].click()

    def jump_to_edit_user_form_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            cell_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            if cell_id == id:
                cells[7].click()
                break

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
            # wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
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

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_emails_like_on_home_page(self, user):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [user.email1, user.email2, user.email3])))

    def merge_emails_of_all_users_from_db(self, users):
        merged_users_email_list = []
        for item in users:
            merged_users_email_list.append(self.merge_emails_like_on_home_page(item))
        return merged_users_email_list

    def merge_phones_like_on_home_page(self, user):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [user.home_phone, user.mobile, user.work_phone, user.second_phone]))))

    def merge_phones_of_all_users_from_db(self, users):
        merged_users_phone_list = []
        for item in users:
            merged_users_phone_list.append(self.merge_phones_like_on_home_page(item))
        return merged_users_phone_list

    def get_info_from_users_list(self, users, key):
        data_list = []
        for item in users:
            if key == 'emails':
                data_list.append(item.all_emails_from_home_page)
            elif key == 'phones':
                data_list.append(item.all_phones_from_home_page)
            elif key == 'lname':
                data_list.append(item.lname)
            elif key == 'fname':
                data_list.append(item.lname)
            elif key == 'address':
                data_list.append(item.address)
        return data_list

    def change_old_users_list(self, old_users, id, new_data):
        for item in old_users:
            if item.id == id:
                item.fname = new_data.fname
                item.lname = new_data.lname
                break
        return old_users

    def choose_filter_on_home_page(self, key):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text('%s' % key)

    def add_user_to_group(self, user_id, group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            cell_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            if cell_id == user_id:
                cells[0].click()
        Select(wd.find_element_by_name("to_group")).select_by_value('%s' % group_id)
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        wd.find_element_by_xpath("//i/a").click()

    def delete_user_from_group(self, user_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[3]/ul/li[1]/a").click()
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            cell_id = cells[0].find_element_by_tag_name("input").get_attribute(
                "value")
            if cell_id == user_id:
                cells[0].click()
        wd.find_element_by_xpath("//input[@name='remove']").click()

    # Оставил для себя на всякий случай
    # def parse_users_list_by_id(self, users, key):
    #     for item in users:
    #         if item.id == key:
    #             break
    #     return item
