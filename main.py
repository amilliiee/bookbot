def main():
    book_path = 'books/frankenstein.txt'
    text = get_words(book_path)
    num_words = get_num_words(text)
    chars_dict = get_dict(text)
    chars_list = get_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for letter in chars_list:
        if not letter["char"].isalpha():
            continue
        print(f"The '{letter['char']}' character was found {letter['num']} times.")
    
    print("--- End report ---")

def get_words(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())

def get_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({'char': ch, 'num': chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(c):
    return c["num"]


main()