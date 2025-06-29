from stats import count_words, count_characters, sort_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = (get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    num_words = count_words(file_contents)
    print(f"Found {num_words} total words")
    num_char = count_characters(file_contents)
    print("--------- Character Count -------")
    char_list = (sort_characters(num_char))
    for item in char_list:
        key, value = item["char"], item["num"]
        if (str.isalpha(key)):
            print (f"{key}: {value}")
    print("============= END ===============")
        
        

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()