from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*BasePageLocators.REGISTRATION_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD2)
        input3.send_keys(password)
        button = self.browser.find_element(*BasePageLocators.REGISTRATION_SUBMIT)
        button.click()        
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "No login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
