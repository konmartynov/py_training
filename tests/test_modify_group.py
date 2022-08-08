from random import randrange
from models.group import Group


def test_modify_group_name(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        group = json_groups
        app.group.create(group)
    r_str = app.gen_random_string()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name=r_str)
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
