import random
from models.user import User


def test_delete_some_user(app, db, json_users, check_ui):
    if len(db.get_user_list()) == 0:
        user = json_users
        app.user.jump_to_add_new_user_form()
        app.user.fill_user_form(user)
        app.user.create_new_user()
        app.return_to_homepage()
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.jump_to_edit_user_form_by_id(user.id)
    app.user.delete_user()
    new_users = db.get_user_list()
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.sort_by_id) == sorted(app.group.get_user_list(), key=User.sort_by_id)
