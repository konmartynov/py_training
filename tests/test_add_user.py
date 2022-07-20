# -*- coding: utf-8 -*-
from models.user import User


def test_add_user(app):
    r_str = app.gen_random_string()
    r_mob = app.gen_random_number()
    mail = r_str + '@email.com'
    old_users = app.user.get_user_list()
    user = User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str, address=r_str,
                home_phone=r_mob, mobile=r_mob, work_phone=r_mob, fax=r_str, email1=mail, email2=mail,
                email3=mail, note=r_str, second_phone=r_mob)
    app.user.jump_to_add_new_user_form()
    app.user.fill_user_form(user)
    app.user.create_new_user()
    app.return_to_homepage()
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == app.user.user_count()
    old_users.append(User(fname=r_str, lname=r_str, id=user.id))
    assert sorted(old_users, key=User.sort_by_id) == sorted(new_users, key=User.sort_by_id)
