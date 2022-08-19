from datetime import datetime
from pony.orm import *
from models.group import Group
from models.user import User
from models.user_in_group import UserInGroup


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        users = Set(lambda: ORMFixture.ORMUser, table='address_in_groups', column='id',
                    reverse='groups', lazy=True)

    class ORMUser(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        fname = Optional(str, column='firstname')
        lname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id',
                     reverse='users', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_users_to_model(self, users):
        def convert(user):
            return User(id=str(user.id), fname=user.fname, lname=user.lname)
        return list(map(convert, users))

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(u for u in ORMFixture.ORMUser if u.deprecated is None))

    @db_session
    def get_users_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(orm_group.users)

    @db_session
    def get_users_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_users_to_model(
            select(u for u in ORMFixture.ORMUser if u.deprecated is None and orm_group not in u.groups))

    @db_session
    def get_groups_with_users(self):
        list_groups = []
        group = self.db.select("group_id from address_in_groups")
        for i in group:
            list_groups.append(UserInGroup(id=str(i)))
        return list_groups

    def convert_contacts_to_model(self, users):
        def convert(user):
            return User(id=str(user.id), fname=user.firstname, lname=user.lastname)
        return list(map(convert, users))
