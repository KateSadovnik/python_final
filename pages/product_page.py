from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def find_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_PAGE).text
        
    def find_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_FROM_PAGE).text
        
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_added_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Product added message is not presented"

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), "Basket price message is not presented"
    
    def find_product_name_from_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_MESSAGE).text
        
    def find_basket_price_from_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE_FROM_MESSAGE).text
        
    def should_be_right_product_name(self, nameToCompare):
        assert self.find_product_name_from_message() == nameToCompare, "Wrong product"

    def should_be_right_price_for_book(self, priceToCompare):
        assert self.find_basket_price_from_message() == priceToCompare, "Wrong price"
