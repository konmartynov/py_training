from random import randrange
from models.group import Group


def test_delete_some_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="for_del", header="for_del_h", footer="for_del_f"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
