test_pytest_frame:用于pytest框架中各种setup及teardown的学习

test_pytest_assume：用于pytest-assume的学习，该框架断言失败时，其后的断言依旧可以继续执行

test_fixture001：测试执行时，有些用例需要登陆，有些无需登陆，setup和teardown无法满足，fixture可以满足

test_fixture002:使用@pytest.fixture()装饰的函数中添加yield，实现类似setup、teardown的功能

test_fixture003:使用conftest.py统一存放被fixture装饰的前置函数

test_fixturn004:使用pytestmark=pytest.mark.usefixtures("open_everyone")，让该模块中所有的用例的前置函数都为open_everyone

test_fixturn005:@pytest.fixture(autouse="true"),让模块中每个用例自动添加login为前置函数，无需将前置函数作为参数传递给用例

test_fixturn006:@pytest.fixture(params=[["豆立航","dlh12378612873"]])前置函数传入参数，request.param提取传入的参数

