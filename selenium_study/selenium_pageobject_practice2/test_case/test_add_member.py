from selenium_study.selenium_pageobject_practice.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index()

    def teardown(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.member.delete_member()

    def test_add_member(self):
        self.member = self.index.goto_add_member().add_member()
        assert "高可乐" in self.member.get_member()

