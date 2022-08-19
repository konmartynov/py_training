import random
from models.user import User
from models.group import Group
from models.user_in_group import UserInGroup


def test_add_some_user_to_group(app, db, orm):
    app.user.choose_filter_on_home_page(key='[none]')
    if len(app.user.get_user_list()) == 0:
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
        app.user.choose_filter_on_home_page(key='[none]')
    if len(db.get_group_list()) == 0:
        group = Group(name="for_add_user", header="to_this", footer="group")
        app.group.create(group)
    old_list_users = db.get_user_in_group_list()
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    users_list = orm.get_users_not_in_group(group)
    user = random.choice(users_list)
    app.user.add_user_to_group(user.id, group)
    new_list_user_in_group = db.get_user_in_group_list()
    old_list_users.append(UserInGroup(id=user.id))
    assert sorted(old_list_users, key=UserInGroup.id_max) == sorted(new_list_user_in_group, key=UserInGroup.id_max)
