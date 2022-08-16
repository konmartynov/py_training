import random
from models.user import User
from models.group import Group


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
    users_list = app.user.get_user_list()
    user = random.choice(users_list)
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    app.user.add_user_to_group(user.id, group.id)
    users_in_groups = orm.get_users_in_group(group)
    # choosed_user_in_group = app.user.parse_users_list_by_id(users_in_groups, key=user.id)
    # assert user.id == choosed_user_in_group.id
    assert user in users_in_groups
