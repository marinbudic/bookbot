import sys

import stats as s

def main():
    
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    # print(get_book_text("books/frankenstein.txt"))
    
    wc = s.word_count(s.get_book_text(path))

    # print(f"{wc} words found in the document")

    char_dict = s.char_count(s.get_book_text(path))
    
    # print(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    char_sorted = s.sort_chars(char_dict)

    for x in char_sorted:
        print(f"{x['char']}: {x['count']}")

    print("============= END ===============")
main()
