def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_counter(book_text)
    char_dic = character_counter(book_text)
    char_list = dic_to_list(char_dic)
    print_report(book_path, num_words, char_list)

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
        if char.isalpha():
            if char in counter:
               counter[char] += 1
            elif char not in counter:
               counter[char] = 1
    return counter

# Create a sorted list from dic
def dic_to_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def print_report(book, words, char_list):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    for item in char_list:
        #print(item)
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


main()