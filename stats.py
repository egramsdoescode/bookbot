def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def find_total_words(book_text):
    return len(book_text.split())


def find_char_frequency(boot_text):
    freq_map = {}

    for c in boot_text:
        lower_c = c.lower()
        if lower_c in freq_map:
            freq_map[lower_c] += 1
        else:
            freq_map[lower_c] = 1

    return freq_map
