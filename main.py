from stats import get_num_words, get_num_letters, sort_letter_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    word_count = get_num_words(book_content)
    letter_count_dict = get_num_letters(book_content)
    sorted_letters_by_count = sort_letter_count(letter_count_dict)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    for d in sorted_letters_by_count:
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
        else:
            continue
    print("============= END ===============")

main()