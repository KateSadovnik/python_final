from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    PRODUCT_NAME_FROM_PAGE = (By.CSS_SELECTOR, "h1")
    PRICE_FROM_PAGE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
    PRODUCT_NAME_FROM_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner")
    BASKET_PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    
    
