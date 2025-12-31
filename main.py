from stats import get_book_text, find_total_words, find_char_frequency


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f" Found {find_total_words(book_text)} total words")
    print(find_char_frequency(book_text))


if __name__ == "__main__":
    main()
