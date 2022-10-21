from models.base import Base


class AttractionDestinationPage(Base):
    def navigate(self):
        self.page.goto("/attractions")

    def search_destination(self, destination, nearby_destination):
        self.page.get_by_test_id("search-input-field").fill(destination)
        self.page.get_by_role("link", name=nearby_destination).click()
        self.page.locator('button[type="submit"]').click()
