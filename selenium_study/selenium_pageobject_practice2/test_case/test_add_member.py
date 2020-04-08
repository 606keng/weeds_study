from selenium_study.selenium_pageobject_practice2.page.index import Index


class TestAddMember:
    def setup(self):
        #定义reuse=True，复用浏览器
        self.index = Index(reuse=True)

    def teardown(self):
        self.member.delete_member()

    def test_add_member(self):
        self.member = self.index.goto_add_member().add_member()
        assert "高可乐" in self.member.get_member()

