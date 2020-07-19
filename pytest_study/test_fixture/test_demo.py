import pytest

@pytest.fixture()
def testfixture():
    print("这是一个fixture")

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

class TestPytest1(object):


    @classmethod
    def setup_class(cls):
        print("setup_class1")

    @classmethod
    def teardown_class(cls):
        print("teardown_class1")

    def setup_method(self):
        print("setup_method1")

    def teardown_method(self):
        print("teardown_method1")

    def test_case1(self):
        print("testcase1,测试用例")

    def testcase2(self,testfixture):
        print("testcase2,测试用例")

    def case3_test(self):
        print("testcase3,测试用例")

    def case4test(self):
        print("testcase4,测试用例")

    @pytest.mark.skip
    def test_case5(self):
        print("testcase5,测试用例")