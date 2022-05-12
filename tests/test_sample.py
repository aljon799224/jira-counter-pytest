import pytest

def add_words(word1, word2):
    return word1 + " " + word2

def to_upperscase(word):
    return word.upper()

def add_and_sub(a, b):
    return (a + b) - b



@pytest.mark.ID_45
@pytest.mark.ID_46
def test_add_words():
    assert add_words("Aljon", "Mendiola") == "Aljon Mendiola"

@pytest.mark.ID_45
@pytest.mark.ID_46
def test_to_uppercase():
    assert to_upperscase("Aljon") == "ALJON"
    
@pytest.mark.ID_46
def test_add_and_sub():
    assert add_and_sub(10, 2) == 10
    
    
