from random import randrange
from models.user import User


def test_modify_some_user(app):
    if app.user.user_count() == 0:
        r_str = app.gen_random_string()
        r_mob = app.gen_random_number()
        mail = r_str + '@email.com'
        user = User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str, address=r_str,
                    home_phone=r_str, mobile=r_mob, work_phone=r_mob, fax=r_str, email=mail, note=r_str,
                    second_phone=r_mob)
        app.user.jump_to_add_new_user_form()
        app.user.fill_user_form(user)
        app.user.create_new_user()
        app.return_to_homepage()
    r_str = app.gen_random_string()
    r_mob = app.gen_random_number()
    mail = r_str + '@email.com'
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str, address=r_str,
                home_phone=r_str, mobile=r_mob, work_phone=r_mob, fax=r_str, email=mail, note=r_str,
                second_phone=r_mob)
    user.id = old_users[index].id
    app.user.jump_to_edit_user_form_by_index(index)
    app.user.fill_user_form(user)
    app.user.update_user()
    app.return_to_homepage()
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[index] = User(fname=r_str, lname=r_str, id=user.id)
    assert sorted(old_users, key=User.sort_by_id) == sorted(new_users, key=User.sort_by_id)
