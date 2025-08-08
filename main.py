from stats import get_word_count, get_char_count, sorter, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_word_count(get_book_text(sys.argv[1]))
    char_dict = get_char_count(get_book_text(sys.argv[1]))
    sorted = sorter(char_dict)
    sorted.sort(reverse=True, key=sort_on)
    print(
        "============ BOOKBOT ============\n",
        f"Analyzing book found at {sys.argv[1]}...\n",
        "----------- Word Count ----------\n",
        f"Found {word_count} total words \n",
        "--------- Character Count -------\n",
    )
    for dick in sorted:
        if dick["name"].isalpha():
            print(f"{dick["name"]}: {dick["num"]}\n")
    print("============= END ===============")
    return

main()