# -*- coding: utf-8 -*-
from models.user import User


def test_add_user(app, db, json_users, check_ui):
    user = json_users
    old_users = db.get_user_list()
    app.user.jump_to_add_new_user_form()
    app.user.fill_user_form(user)
    app.user.create_new_user()
    app.return_to_homepage()
    new_users = db.get_user_list()
    assert len(old_users) + 1 == app.user.user_count()
    old_users.append(User(fname=user.fname, lname=user.lname, id=user.id))
    assert old_users == new_users
    if check_ui:
        assert sorted(old_users, key=User.sort_by_id) == sorted(new_users, key=User.sort_by_id)
