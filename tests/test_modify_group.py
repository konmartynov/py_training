from models.group import Group


# def test_modify_first_group(app):
#     if app.group.group_count() == 0:
#         app.group.create(Group(name="for_mod", header="for_mod_h", footer="for_mod_f"))
#     r_str = app.gen_random_string()
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(name=r_str, header=r_str, footer=r_str))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.group_count() == 0:
        group = Group(name="for_mod", header="for_mod_h", footer="for_mod_f")
        app.group.create(group)
    r_str = app.gen_random_string()
    old_groups = app.group.get_group_list()
    group = Group(name=r_str)
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.group_count() == 0:
#         app.group.create(Group(name="for_mod", header="for_mod_h", footer="for_mod_f"))
#     r_str = app.gen_random_string()
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header=r_str))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
