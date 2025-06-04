def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters = {}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_letter_count(letter_count_dict):
    letter_count_list = []
    for letter, count in letter_count_dict.items():
        letter_count_list.append({"char": letter, "num": count})
    sorted_letters = sorted(letter_count_list, key=lambda x: x["num"], reverse=True)
    return sorted_letters