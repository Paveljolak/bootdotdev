from stats import get_book_text, count_words, count_characters, sort_list_of_dicts
import sys

def main():

    # check whether the length of args is correct
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # grab the book
    text = get_book_text(sys.argv[1])

    # grab and print the count of words
    count = count_words(text)
    print(f"Found {count} total words")

    # grab the count of chars
    chars = count_characters(text)

    # create a proper list of dicts
    list_of_dicts = sort_list_of_dicts(chars)

    # check whether is alpha
    for char in list_of_dicts:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

# Main fun
main()