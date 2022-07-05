from models.group import Group


def test_delete_first_group(app):
    app.group.create(Group(name="for_del", header="for_del_h", footer="for_del_f"))
    app.group.delete_first_group()
