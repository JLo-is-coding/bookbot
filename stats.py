def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char not in characters:
            characters[char] = 0
        characters[char] = characters[char] +1
    return characters

def sort_characters(char):
    sorted_list = []
    for i in char:
        item = {"char" : i, "num": char[i]}
        sorted_list.append(item)
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list
    

def sort_by(item):
    return item["num"]