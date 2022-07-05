# -*- coding: utf-8 -*-
from models.user import User


def test_add_user(app):
    r_str = app.gen_random_string()
    r_mob = app.gen_random_number()
    mail = r_str + '@email.com'
    app.user.jump_to_add_new_user_form()
    app.user.fill_user_form(User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str,
                                 address=r_str, home=r_str, mobile=r_mob, work_phone=r_mob, fax=r_str,
                                 email=mail, note=r_str))
    app.user.create_new_user()
    app.return_to_homepage()
