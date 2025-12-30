def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    print(file_contents)


get_book_text("books/frankenstein.txt")
