def make_snippet(str1):
    split_string = str1.split()
    if len(split_string) > 5:
        new_string_1 = " ".join(split_string[:5]) + " ..."
        return new_string_1
    else:
        return str1
 

print(make_snippet("hello my name is potato man"))