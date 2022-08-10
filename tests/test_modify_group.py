import random
from models.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        group = Group(name="for_mod", header="for_mod_h", footer="for_mod_f")
        app.group.create(group)
    r_str = app.gen_random_string()
    group = Group(name=r_str)
    old_groups = db.get_group_list()
    group_choosed = random.choice(old_groups)
    app.group.modify_group_by_id(group_choosed.id, group)
    new_groups = db.get_group_list()
    changed_old_groups = app.group.change_old_groups_list(old_groups, group_choosed.id, new_data=Group(name=r_str))
    assert changed_old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
