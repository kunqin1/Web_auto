import pytest
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as td


# 调用前置方法：back_login
@pytest.mark.usefixtures("back_login")
class TestLogin:

    # # 逆向场景 - 登陆失败 - 数据格式无效
    @pytest.mark.parametrize("case", td.invalid_data)
    def test_login_failed(self, case, back_login):
        LoginPage(back_login).login(case["user"], case["passwd"])
        res = LoginPage(back_login).get_error_msg_from_login_area()
        LoginPage(back_login).close_login_window()
        assert res == case['check']

    # 正向场景 - 登陆成功
    def test_login_success(self, back_login):
        LoginPage(back_login).login(*td.valid_user)
        assert LoginPage(back_login).get_userName()
