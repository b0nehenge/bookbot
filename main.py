import sys

from stats import generate_sorted_list, get_character_count, get_num_words


def get_book_text(file):
    print(f"Analyzing book found at {file}")
    with open(file) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    print("============ BOOKBOT ============")
    text = get_book_text(sys.argv[1])

    word_count = get_num_words(text)
    character_count = get_character_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_list = generate_sorted_list(character_count)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
