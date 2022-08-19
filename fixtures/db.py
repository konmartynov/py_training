import pymysql.cursors
from models.group import Group
from models.user import User
from models.user_in_group import UserInGroup


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, fname, lname) = row
                list.append(User(id=str(id), fname=fname, lname=lname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_users_info(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, "
                           "work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, fname, lname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(User(id=str(id), fname=fname, lname=lname, address=address, email1=email, email2=email2,
                                 email3=email3, home_phone=home, mobile=mobile, work_phone=work, second_phone=phone2))
        finally:
            cursor.close()
        return list

    def get_user_in_group_list(self):
        user_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where deprecated is Null")
            for row in cursor:
                (user_id, group_id) = row
                user_list.append(UserInGroup(id=str(user_id), group_id=str(group_id)))
        finally:
            cursor.close()
        return user_list
