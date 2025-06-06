import sys
from stats import get_number_of_words
from stats import get_count_per_character
from stats import get_count_per_character_sorted

def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    counts = get_count_per_character(book_text)
    sorted_counts = get_count_per_character_sorted(counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
