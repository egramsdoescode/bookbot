import sys

from stats import (
    get_book_text,
    find_total_words,
    find_char_frequency,
    format_freq_map,
    generate_report,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = find_total_words(book_text)
    char_frequency = find_char_frequency(book_text)

    map_list = format_freq_map(char_frequency)

    generate_report(filepath, word_count, map_list)


if __name__ == "__main__":
    main()
