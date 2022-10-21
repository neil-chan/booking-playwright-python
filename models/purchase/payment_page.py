from models.base import Base


class PaymentPage(Base):
    @property
    def total_price(self):
        return self.page.get_by_test_id("price-breakdown-total").nth(2)

    def inputName(self, name):
        self.page.frame_locator("iframe").get_by_label("Cardholder's Name*").fill(name)

    def inputCreditCard(self, creditCard):
        self.page.frame_locator("iframe").locator("input[type=\"tel\"]").fill(creditCard)
    
    def inputExpiryDate(self, expiryDate):
        self.page.frame_locator("iframe").get_by_role("textbox", name="MM/YY").fill(expiryDate)

    def inputCVC(self, cvc):
        self.page.frame_locator("iframe").get_by_label("CVC*").fill(cvc)
    
    def fillOutCreditCardForm(self, name, card, date, cvc):
        self.inputName(name)
        self.inputCreditCard(card)
        self.inputExpiryDate(date)
        self.inputCVC(cvc)
