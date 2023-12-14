def main():
    book = "books/frankenstein.txt"
    txt = get_text(book)
    wd_ct = get_wd_ct(txt)
    letters = get_let_ct(txt)
    print(f'Document has {wd_ct} words')
    for pair in letters:
        print(f'{pair[0]}: {pair[1]}')

def get_wd_ct(text):
    wds = text.split()
    return len(wds)

def get_let_ct(text):
    letters = {}
    txt = text.lower().split()
    for word in txt:
        for letter in word:
            if letter.isalpha():
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1
    letters = list(letters.items())
    sorted_letters = sorted(letters)
    return sorted_letters


def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()