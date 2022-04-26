import pytest
from all_func import greater_than, less_than, is_equal

class TestComparison:
    
    @pytest.mark.ID_46
    @pytest.mark.ID_47
    @pytest.mark.ID_48
    def test_greater_than(self):
        assert greater_than(5, 2) == True
    
    @pytest.mark.ID_46
    @pytest.mark.ID_47
    @pytest.mark.ID_48
    def test_less_than(self):
        assert less_than(2, 5) == True
    
    @pytest.mark.ID_46
    @pytest.mark.ID_47
    @pytest.mark.ID_48
    def test_is_equal(self):
        assert is_equal(5, 5) == True
    