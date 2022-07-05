from models.group import Group


def test_modify_first_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="for_mod", header="for_mod_h", footer="for_mod_f"))
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(name=r_str, header=r_str, footer=r_str))


def test_modify_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="for_mod", header="for_mod_h", footer="for_mod_f"))
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(name=r_str))


def test_modify_group_header(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="for_mod", header="for_mod_h", footer="for_mod_f"))
    r_str = app.gen_random_string()
    app.group.modify_first_group(Group(header=r_str))
