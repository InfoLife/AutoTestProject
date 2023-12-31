from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, 'h1:nth-child(1)')
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, "#messages div:first-child div strong")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) div strong')

class BasketPageLocators:
    PRODUCT_PRESENT = (By.CSS_SELECTOR, ".col-sm-6")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
