from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class LoginPage:
    __unTB = (By.ID, "username")
    __pwTB = (By.NAME, "pwd")
    __loginBTN = (By.XPATH, "//div[.='Login ']")
    __errmsg=(By.XPATH,"//span[contains(text(),'invalid')]")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, un):
        self.driver.find_element(*self.__unTB).send_keys(un)

    def set_password(self, pw):
        self.driver.find_element(*self.__pwTB).send_keys(pw)

    def click_loginbutton(self):
        self.driver.find_element(*self.__loginBTN).click()

    def verify_err_msg_displayed(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__errmsg))
            print("Err Msg is displayed")
            return True
        except:
            print("Err msg is not displayed")
            return False
