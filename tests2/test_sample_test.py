import pytest

def get_length_word(word):
    return len(word)

def get_max(numbers):
    return max(numbers)
    
def get_min(numbers):
    return min(numbers)

class TestSample:
    
    @pytest.mark.ID_63
    @pytest.mark.ID_61
    def test_get_length_word(self):
        assert get_length_word("aljon") == 5
        
    @pytest.mark.ID_63
    @pytest.mark.ID_62
    def test_get_max(self):
        assert get_max([1,2,3]) == 3
        
    @pytest.mark.ID_63
    @pytest.mark.ID_42
    def test_get_min(self):
        assert get_min([1,2,3]) == 1
        
    