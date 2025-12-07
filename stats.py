def get_num_words(text):
    return len(text.split())


def get_character_count(text):
    map = {}

    for char in text:
        lower_char = char.lower()
        if not lower_char.isalpha():
            continue

        if lower_char in map:
            map[lower_char] += 1
        else:
            map[lower_char] = 1

    return map


def generate_sorted_list(dic):
    char_list = []
    for key in dic:
        char_list.append({"char": key, "num": dic[key]})

    char_list.sort(reverse=True, key=lambda list: list["num"])
    return char_list
