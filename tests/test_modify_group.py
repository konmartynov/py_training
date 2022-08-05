from random import randrange
from models.group import Group


def test_modify_group_name(app, db, json_groups, check_ui):
    if app.group.group_count() == 0:
        group = json_groups
        app.group.create(group)
    r_str = app.gen_random_string()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name=r_str)
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
