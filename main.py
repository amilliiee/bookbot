import sys
from stats import get_word_count, get_letter_count, sort_letter_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        
    book = get_book_text(book_path)
    words = get_word_count(book)
    letters = get_letter_count(book)
    sorted_letters = sort_letter_count(letters)
    report = f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {words} total words
    --------- Character Count -------
    """
    
    print(report)
    for ltr in sorted_letters:
        if ltr["char"].isalpha():
            print(f"{ltr['char']}: {ltr['count']}")
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

    
main()