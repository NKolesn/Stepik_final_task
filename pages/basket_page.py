from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        languages = {
    "لعربيّة": "سلة التسوق فارغة",
    "català": "La seva cistella està buida.",
    "česky": "Váš košík je prázdný.",
    "dansk": "Din indkøbskurv er tom.",
    "Deutsch": "Ihr Warenkorb ist leer.",
    "British English": "Your basket is empty.",
    "Ελληνικά": "Το καλάθι σας είναι άδειο.",
    "español": "Tu carrito esta vacío.",
    "suomi": "Korisi on tyhjä",
    "français": "Votre panier est vide.",
    "italiano": "Il tuo carrello è vuoto.",
    "한국어": "장바구니가 비었습니다.",
    "Nederlands": "Je winkelmand is leeg",
    "polski": "Twój koszyk jest pusty.",
    "Português": "O carrinho está vazio.",
    "Português Brasileiro": "Sua cesta está vazia.",
    "Română": "Cosul tau este gol.",
    "Русский": "Ваша корзина пуста",
    "Slovensky": "Váš košík je prázdny",
    "Українська": "Ваш кошик пустий.",
    "简体中文": "Your basket is empty.",
    }
        current_language_elt = self.browser.find_element(*BasePageLocators.CURRENT_LANGUAGE)
        current_language = languages.get(current_language_elt.text)
        basket_isempty = self.browser.find_element(*BasePageLocators.BASKET_ISEMPTY)
        assert current_language in basket_isempty.text, "Message isn't present"
        
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEM_LOCATOR), \
           "Product item is presented, but should not be"

