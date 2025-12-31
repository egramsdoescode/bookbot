def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def find_total_words(book_text):
    return len(book_text.split()) 
