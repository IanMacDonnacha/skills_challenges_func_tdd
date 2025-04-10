from lib.countwords import *

def test_return_empty_string():
    result = count_words("")
    assert result == ""

def test_how_many_words_in_string_5():
    result = count_words("hello my name is ian")
    assert result == 5

def test_how_many_words_in_string_10():
    result = count_words("hello my name is ian and I have a cat")
    assert result == 10

