import pytest
from all_func import  add, sub, mul, div

class TestCalculator:
    
    # @pytest.mark.ID_42
    @pytest.mark.ID_43
    @pytest.mark.ID_46
    def test_add(self):
        assert add(1, 5) == 6
        
    # @pytest.mark.ID_42
    @pytest.mark.ID_43
    @pytest.mark.ID_46
    def test_sub(self):
        assert sub(5, 3) == 2
        
    @pytest.mark.ID_42
    @pytest.mark.ID_43
    @pytest.mark.ID_46
    def test_mul(self):
        assert mul(2, 3) == 6
        
    @pytest.mark.ID_42
    @pytest.mark.ID_46
    def test_div(self):
        assert div(10, 5) == 2
        

