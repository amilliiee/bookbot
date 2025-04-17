def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_letter_count(book_text):
    words = book_text.lower()
    letters = {}
    
    for char in words:
        if not char in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters

def sort_letter_count(letter_count):
    char_list = dict_to_list(letter_count)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    char_list = []
    
    for char, ct in dict.items():
        char_dict = { "char": char, "count": ct }
        char_list.append(char_dict)
    
    return char_list