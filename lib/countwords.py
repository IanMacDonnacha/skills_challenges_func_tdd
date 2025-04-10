def count_words(str1):
    split_list = str1.split()
    if len(split_list) > 0:
        return len(split_list)
    else:
        return str1