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