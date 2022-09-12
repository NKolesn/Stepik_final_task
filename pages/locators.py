from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    TITLE_LOCATOR = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    ITEM_LOCATOR = (By.CSS_SELECTOR, ".basket-items")
    BASKET_ISEMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    CURRENT_LANGUAGE = (By.CSS_SELECTOR, '[selected="selected"]')
    

    


