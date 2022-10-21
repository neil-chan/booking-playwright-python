from models.base import Base


class AttractionSearchPage(Base):
    def search_attraction(self, attraction):
        self.page.get_by_test_id("search-input-field").fill(attraction)
        self.page.get_by_test_id("search-input-field").press("Enter")

    def click_attraction(self, title):
        with self.page.expect_popup() as popup_info:
            self.page.locator(f'[title="{title}"]').click()
        return popup_info.value
