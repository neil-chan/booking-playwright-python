from playwright.sync_api import Page, expect
from models.attraction.destination_page import AttractionDestinationPage 
from models.attraction.search_page import AttractionSearchPage
from models.attraction.details_page import AttractionDetailsPage
from models.purchase.user_info_page import UserInfoPage
from models.purchase.payment_page import PaymentPage


class TestBookAttraction:
    def test_complete_booking_attraction(self, page: Page) -> None:
        page.context.clear_cookies()
        destination_page = AttractionDestinationPage(page)
        search_page = AttractionSearchPage(page)

        # Search for the destination
        destination_page.navigate()
        destination_page.search_destination("Vancouver, British Columbia", "Vancouver, British Columbia Canada")

        # Search for the Attraction
        search_page.search_attraction("Capilano")
        page1 = search_page.click_attraction("Capilano Suspension Bridge Park Admission")

        # Navigating to Attraction details page
        details_page = AttractionDetailsPage(page1)
        details_page.select_date("29 October 2022")
        details_page.select_timeslot("05:00 PM")
        details_page.number_of_adult_ticket(2)
        details_page.select_ticket()

        # Filling out user info page
        user_info_page = UserInfoPage(page1)
        user_info_page.fillOutForm("Neil", "Villegas", "neilvillegas@gmail.com", "7785551212")
        total_price = user_info_page.get_total_price()
        user_info_page.proceed_payment()

        # Checking Payment Page
        payment_page = PaymentPage(page1)
        payment_page.fillOutCreditCardForm("Neil Villegas", "4519142289341212", "01/23", "123")
        expect(payment_page.total_price).to_contain_text([total_price])
