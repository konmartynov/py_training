from models.group import Group


def test_modify_first_group(app):
    app.group.create(Group(name="for_del", header="for_del_h", footer="for_del_f"))
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(name=r_str, header=r_str, footer=r_str))


def test_modify_group_name(app):
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(name=r_str))


def test_modify_group_header(app):
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(header=r_str))
