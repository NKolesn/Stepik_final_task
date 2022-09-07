from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        title_selector_elt = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
        title_selector = title_selector_elt.text
        assert f"{title_selector} has been added to your basket" in success_message.text, "Message doesn't match"

    def should_be_the_same_price():
        book_price_elt = self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color")
        basket_price_elt = self.browser.find_element(By.CSS_SELECTOR, ".basket-mini")
        assert book_price_elt.text == basket_price_elt.text, "Price doesn't match"
        
    
