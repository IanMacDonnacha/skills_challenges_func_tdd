from lib.personal_diary_system import *

## Take a string and return the same string

# def test_take_string_and_return():
#     return_string = make_snippet("hello my name is potato man")
#     assert return_string == "hello my name is potato man"

## Take the inputted string and return a list

# def test_take_string_and_return_string_as_list():
#     return_string = make_snippet("hello my name is potato man")
#     assert return_string == ["hello", "my", "name", "is", "potato", "man"]

## Take the resulting list and return first 5 words

# def test_slice_first_5_words_of_new_list():
#     return_list = make_snippet("hello my name is potato man")
#     assert return_list == ["hello", "my", "name", "is", "potato"]

## Take the resulting 5 word list and return as a new string

# def test_convert_list_back_to_string():
#     return_string = make_snippet("hello my name is potato man")
#     assert return_string == "hello my name is potato"

## check if string has 5 words and return the same string

def test_string_if_it_has_5_words_and_return():
    return_string = make_snippet("hello my name is potato")
    assert return_string == "hello my name is potato"

def test_string_if_it_has_5_words_and_return_with_3_dots():
    return_string = make_snippet("hello my name is potato man")
    assert return_string == "hello my name is potato ..."    

