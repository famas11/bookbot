def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(word_counter(book_text))
#    print(book_text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

main()