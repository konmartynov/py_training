import re
from random import randrange
from models.user import User


def test_compare_user_data_on_home_page_and_edit_form(app):
    if app.user.user_count() == 0:
        r_str = app.gen_random_string()
        r_mob = app.gen_random_number()
        mail = r_str + '@email.com'
        user = User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str, address=r_str,
                    home_phone=r_mob, mobile=r_mob, work_phone=r_mob, fax=r_str, email1=mail, email2=mail,
                    email3=mail, note=r_str, second_phone=r_mob)
        app.user.jump_to_add_new_user_form()
        app.user.fill_user_form(user)
        app.user.create_new_user()
        app.return_to_homepage()
    users_list_on_home_page = app.user.get_user_list()
    index = randrange(len(users_list_on_home_page))
    user_from_home_page = app.user.get_user_list()[index]
    user_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert user_from_home_page.fname == user_from_edit_page.fname
    assert user_from_home_page.lname == user_from_edit_page.lname
    assert user_from_home_page.address == user_from_edit_page.address
    assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [user.email1, user.email2, user.email3])))

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.home_phone, user.work_phone, user.mobile, user.second_phone]))))
