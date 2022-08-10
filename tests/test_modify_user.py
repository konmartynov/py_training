import random
from models.user import User


def test_modify_some_user(app, db, check_ui):
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
    r_str = app.gen_random_string()
    r_mob = app.gen_random_number()
    mail = r_str + '@email.com'
    user = User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str, address=r_str,
                home_phone=r_mob, mobile=r_mob, work_phone=r_mob, fax=r_str, email1=mail, email2=mail,
                email3=mail, note=r_str, second_phone=r_mob)
    old_users = db.get_user_list()
    user_choosed = random.choice(old_users)
    app.user.jump_to_edit_user_form_by_id(user_choosed.id)
    app.user.fill_user_form(user)
    app.user.update_user()
    app.return_to_homepage()
    new_users = db.get_user_list()
    changed_old_users = app.user.change_old_users_list(old_users, user_choosed.id, new_data=User(fname=r_str, lname=r_str))
    assert changed_old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.sort_by_id) == sorted(app.group.get_user_list(), key=User.sort_by_id)
