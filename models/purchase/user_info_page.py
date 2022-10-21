from models.base import Base


class UserInfoPage(Base):
    def inputFirstName(self, firstName):
        self.page.get_by_label("First Name*").fill(firstName)

    def inputLastName(self, lastName):
        self.page.get_by_label("Last name*").fill(lastName)

    def inputEmail(self, email):
        self.page.get_by_role("textbox", name="Email Address *").fill(email)
    
    def confirmEmail(self, email):
        self.page.get_by_label("Confirm email address*").fill(email)

    def inputPhoneNumber(self, phone):
        self.page.get_by_label("Phone (mobile number preferred) *").fill(phone)

    def fillOutForm(self, firstName, lastName, email, phone):
        self.inputFirstName(firstName)
        self.inputLastName(lastName)
        self.inputEmail(email)
        self.confirmEmail(email)
        self.inputPhoneNumber(phone)
    
    def proceed_payment(self):
        self.page.get_by_role("button", name="Next").click()