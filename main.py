def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_counter(book_text)
    char_count = character_counter(book_text)
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def character_counter(text):
    counter = {}

    for char in text:
        char = char.lower()
        if char in counter:
            counter[char] += 1
        elif char not in counter:
            counter[char] = 1
    return counter

main()