import re


def test_phones_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.home_phone == clear(user_from_edit_page.home_phone)
    assert user_from_home_page.mobile == clear(user_from_edit_page.mobile)
    assert user_from_home_page.work_phone == clear(user_from_edit_page.work_phone)

def test_phones_on_user_view_page(app):
    user_from_view_page = app.user.get_user_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.home_phone == user_from_edit_page.home_phone
    assert user_from_view_page.mobile == user_from_edit_page.mobile
    assert user_from_view_page.work_phone == user_from_edit_page.work_phone

def clear(s):
    return re.sub("[() -]", "", s)
