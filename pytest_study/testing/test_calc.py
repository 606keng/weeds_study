import sys
import pytest
from python.calc import Calc

@pytest.fixture(scope="module", params=[1,2,3])
def data(request):
    yield request.params

class TestCalc:
    @pytest.mark.parametrize(['a','b'] , [(1,2), (-1,2), (2,-1)])
    def test_add(self,a,b):
        calc = Calc()
        print(data)
        assert a + b == calc.add(a, b)
    @pytest.mark.parametrize(['a','b'] , [(1,2), (-1,2), (2,-1), (0,1), (1,1)])
    def test_div(self,a ,b):
        calc = Calc()
        assert a/b == calc.div(a,b)

if __name__ == '__main__':
    pytest.main("-s")