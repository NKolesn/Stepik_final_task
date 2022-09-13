from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_ISEMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    CURRENT_LANGUAGE = (By.CSS_SELECTOR, '[selected="selected"]')
    ITEM_LOCATOR = (By.CSS_SELECTOR, ".basket-items")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    TITLE_LOCATOR = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    
    

    

    


