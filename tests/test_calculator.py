from re import S
import pytest
from src.calculator import Calculator

class TestCalculator():

    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self): #can be teardown_method or teardown_class
        pass

    # def setup_method(self):
    #     self.calc = Calculator()
    #     print("Setup executado antes de cada teste")

    @pytest.mark.skip(reason="not implemented yet")
    def test_addition(self):
        assert self.calc.addition(2,2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(2,2) == 0

    def test_division(self):
        assert self.calc.division(2,2) == 1
    
    def test_difference(self):
        assert self.calc.difference(2,2) == 4

    ##PYTHON CONSOLE COMANDS
    #pytest -v -- show a verbose code
    #pytest -s -- show all of strings (prints)
    #pytest -- run all tests
    #pytest --collect-only  (display all functions)