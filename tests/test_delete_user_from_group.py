import random
from models.user import User
from models.group import Group


def test_delete_some_user_from_group(app, db, orm):
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
    if len(db.get_group_list()) == 0:
        group = Group(name="for_del_user", header="from_this", footer="group")
        app.group.create(group)
    old_list_user = orm.get_groups_with_users()
    group = random.choice(old_list_user)
    user_in_group = orm.get_users_in_group(group)
    user = random.choice(user_in_group)
    app.user.delete_user_from_group(user.id, group)
    new_list_user_in_group = orm.get_users_in_group(group)
    user_in_group.remove(user)
    assert user_in_group == new_list_user_in_group
