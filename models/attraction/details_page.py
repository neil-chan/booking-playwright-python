from models.base import Base


class AttractionDetailsPage(Base):
    def select_date(self, dateselected):
        self.page.get_by_test_id("datepicker").click()
        self.page.get_by_role("checkbox", name=dateselected).click()

    def select_timeslot(self, timeslot):
        self.page.locator('select[name="timeSlot"]').select_option(label=timeslot)
        
    def number_of_adult_ticket(self, ticket_number):
        for x in range(ticket_number):
            self.page.locator(".e98c626f34 > button:nth-child(3)").first.click()
    
    def select_ticket(self):
        self.page.get_by_test_id("select-ticket").click()
