def get_number_of_words(text):
    return len(text.split())


def get_count_per_character(text):
    count = {}
    for char in text:
        ch = char.lower()
        if not ch in count:
            count[ch] = 0
        count[ch] += 1
    return count


def sort_on(dict):
    return dict["num"]

def get_count_per_character_sorted(counts):
    result = []
    for key in counts:
        result.append({"char": key, "num": counts[key]})
    result.sort(reverse=True, key=sort_on)
    return result