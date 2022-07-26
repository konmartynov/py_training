# -*- coding: utf-8 -*-
import pytest
from models.user import User


@pytest.mark.parametrize("user", test_data, ids=[repr(x) for x in test_data])
def test_add_user(app, json_user):
    old_users = app.user.get_user_list()
    app.user.jump_to_add_new_user_form()
    app.user.fill_user_form(json_user)
    app.user.create_new_user()
    app.return_to_homepage()
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == app.user.user_count()
    old_users.append(User(fname=user.fname, lname=user.lname, id=user.id))
    assert sorted(old_users, key=User.sort_by_id) == sorted(new_users, key=User.sort_by_id)
