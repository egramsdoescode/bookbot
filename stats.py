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


def format_freq_map(map):
    def sort_on(items):
        return items["num"]

    result = []

    for k, v in map.items():
        if k.isalpha():
            result.append({"char": k, "num": v})

    result.sort(reverse=True, key=sort_on)

    return result


def generate_report(filepath, word_count, map_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book count at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for map in map_list:
        char, num = map.items()
        print(f"{char[1]}: {num[1]}")

    print("============= END ===============")
