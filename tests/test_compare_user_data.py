import re
from random import randrange
from models.user import User


def test_compare_user_data_on_home_page_and_edit_form(app, db):
    if len(db.get_user_list()) == 0:
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
    assert user_from_home_page.all_emails_from_home_page == app.user.merge_emails_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_phones_from_home_page == app.user.merge_phones_like_on_home_page(user_from_edit_page)


def test_compare_users_data_on_home_page_and_db(app, db):
    if len(db.get_user_list()) == 0:
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
    user_from_home_page = sorted(app.user.get_user_list(), key=User.sort_by_id)
    users_list_from_db = sorted(db.get_users_info(), key=User.sort_by_id)
    assert app.user.get_info_from_users_list(user_from_home_page, key='emails') == \
           app.user.merge_emails_of_all_users_from_db(users_list_from_db)
    assert app.user.get_info_from_users_list(user_from_home_page, key='phones') == \
           app.user.merge_phones_of_all_users_from_db(users_list_from_db)
    assert app.user.get_info_from_users_list(user_from_home_page, key='lname') == \
           app.user.get_info_from_users_list(users_list_from_db, key='lname')
    assert app.user.get_info_from_users_list(user_from_home_page,key='fname') == \
           app.user.get_info_from_users_list(users_list_from_db, key='fname')
    assert app.user.get_info_from_users_list(user_from_home_page,key='address') == \
           app.user.get_info_from_users_list(users_list_from_db, key='address')
