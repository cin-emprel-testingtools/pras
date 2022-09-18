from re import S
import pytest
from src.generals import Generals


class TestGenerals():

    def setup_class(self):
        self.calc = Generals()

    def teardown_class(self): #can be teardown_method or teardown_class
        pass

    def test_biggerThan(self):
        assert self.calc.biggerThan(2,3) == 3
    
    def test_smallerThan(self):
        assert self.calc.smallerThan(2,3) == 2

    @pytest.mark.skip(reason="not implemented yet")
    def test_passes_but_bad_style(x):
        try:
            x = 1 / 0
            assert False
        except ZeroDivisionError:
            assert True