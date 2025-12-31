from stats import get_book_text, find_total_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f" Found {find_total_words(book_text)} total words")


main()
