from models.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="for_del", header="for_del_h", footer="for_del_f"))
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(name=r_str, header=r_str, footer=r_str))
    app.session.logout()
