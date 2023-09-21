from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login/" in self.browser.current_url, "word '/login/' not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_registration.send_keys(email)
        password_registration = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_registration.send_keys(password)
        password_confirmation = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password_confirmation.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
