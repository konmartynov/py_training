# -*- coding: utf-8 -*-
import pytest
import random
import string
from models.user import User


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_phone():
    symbols = '+7' + ''.join(random.choice(string.digits) for i in range(10))
    return symbols


def random_mail():
    symbols = ''.join(random.choice(string.ascii_letters) for i in range(5)) + '@email.com'
    return symbols


test_data = [
    User(fname=random_string("fname", 10), mname=random_string("mname", 15), lname=random_string("lname", 15),
         nickname=random_string("nickname", 10), company=random_string("company", 10), address=random_string("address", 10),
         home_phone=random_phone(), mobile=random_phone(), work_phone=random_phone(), fax=random_string("fax", 5),
         email1=random_mail(), email2=random_mail(), email3=random_mail(), note=random_string("note", 10),
         second_phone=random_phone())
    for i in range(2)
    ]


@pytest.mark.parametrize("user", test_data, ids=[repr(x) for x in test_data])
def test_add_user(app, user):
    old_users = app.user.get_user_list()
    app.user.jump_to_add_new_user_form()
    app.user.fill_user_form(user)
    app.user.create_new_user()
    app.return_to_homepage()
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == app.user.user_count()
    old_users.append(User(fname=user.fname, lname=user.lname, id=user.id))
    assert sorted(old_users, key=User.sort_by_id) == sorted(new_users, key=User.sort_by_id)
