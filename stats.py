def get_word_count(text):
    split_text = text.split()
    word_count = 0
    for i in split_text:
        word_count += 1
    return word_count

def get_char_count(text):
    text_small = text.lower()
    output = {}
    for char in text_small:
        if char not in output:
            output[char] = 1
        elif char in output:
            output[char] += 1
        else:
            "sumting wong"
    return output

def sorter(dictionary):
    list_of_dictionaries = []
    for char in dictionary:
        small_dict = {"name": char, "num": dictionary[char]}
        list_of_dictionaries.append(small_dict)
    return list_of_dictionaries

def sort_on(items):
    return items["num"]


