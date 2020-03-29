from pytest_study.test_appium.page.app import App


class TestSearch:
    def test_search(self):
        # App().start().main().goto_market().goto_search().search("id")
        App().start().main().goto_market().goto_search().search("id")