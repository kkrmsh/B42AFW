import pytest
from generic.base_setup import Base_Setup
from generic.utility import Excel
from page.login_page import LoginPage


class Test_InvalidLogin(Base_Setup):

    @pytest.mark.run(order=2)
    def test_invalid_login(self):

        un=Excel.get_data(self.xl_path,"invalid_login",2,1)
        pw=Excel.get_data(self.xl_path,"invalid_login",2,2)


        # 1.	Enter invalid username: abcd
        login_page = LoginPage(self.driver)
        login_page.set_username(un)

        # 2.	Enter invalid password: xyz
        login_page.set_password(pw)

        # 3.	Click on login button
        login_page.click_loginbutton()

        # 4.	Err message should be displayed
        result = login_page.verify_err_msg_displayed(self.wait)
        assert result
