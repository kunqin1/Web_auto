import pytest
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as td


# 调用前置方法：back_login
@pytest.mark.usefixtures("login")
class TestLogin:

    # # 逆向场景 - 登陆失败 - 数据格式无效
    @pytest.mark.parametrize("case", td.invalid_data)
    def test_login_failed(self, case, login):
        LoginPage(login).login(case["user"], case["passwd"])
        res = LoginPage(login).get_error_msg_from_login_area()
        LoginPage(login).close_login_window()
        assert res == case['check']

    # 正向场景 - 登陆成功
    def test_login_success(self, login):
        LoginPage(login).login(*td.valid_user)
        assert LoginPage(login).get_userName()
