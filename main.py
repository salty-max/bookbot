def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    generate_report(book_path, book)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(dict):
    return dict["n"]

def get_chars_sorted_list(chars_dict):
    chars_list = []
    for k in chars_dict:
        chars_list.append({ "char": k, "n": chars_dict[k] })
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def generate_report(path, book):
    print(f"--- Begin report of {path} ---")
    words = count_words(book)
    print(f"{words} words found in the document\n")
    chars_dict = get_chars_dict(book)
    chars_list = get_chars_sorted_list(chars_dict)
    for cd in chars_list:
        if not cd["char"].isalpha():
            continue
        print(f"The {cd["char"]} character was found {cd["n"]} times")
    print("--- End report ---")

main()
