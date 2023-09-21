from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert 'empty' in basket_message, "Basket is not empty"

    def should_be_no_products(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_PRESENT), "Products shouldn't be present"
