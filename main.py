from stats import count_words, count_characters

def main():
    file_contents = (get_book_text("books/frankenstein.txt"))
    num_words = count_words(file_contents)
    print (f"{num_words} words found in the document")
    num_char = count_characters(file_contents)
    print (num_char)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()