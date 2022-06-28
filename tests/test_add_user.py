# -*- coding: utf-8 -*-
from random import choice
from string import ascii_letters, digits
from models.user import User


def test_add_user(app):
    r_str = ''.join(choice(ascii_letters) for i in range(5))
    r_mob = '+7' + ''.join(choice(digits) for i in range(10))
    mail = r_str + '@email.com'
    app.session.login(username="admin", password="secret")
    app.user.add_new(User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str,
                          address=r_str, home=r_str, mobile=r_mob, work_phone=r_mob, fax=r_str, email=mail,
                          note=r_str))
    app.session.logout()
