from random import randrange
from models.user import User


def test_delete_some_user(app):
    r_str = app.gen_random_string()
    r_mob = app.gen_random_number()
    mail = r_str + '@email.com'
    if app.user.user_count() == 0:
        user = User(fname=r_str, mname=r_str, lname=r_str, nickname=r_str, company=r_str, address=r_str,
                    home_phone=r_str, mobile=r_mob, work_phone=r_mob, fax=r_str, email1=mail, note=r_str,
                    second_phone=r_mob)
        app.user.jump_to_add_new_user_form()
        app.user.fill_user_form(user)
        app.user.create_new_user()
        app.return_to_homepage()
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.jump_to_edit_user_form_by_index(index)
    app.user.delete_user()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index+1] = []
    assert old_users == new_users
