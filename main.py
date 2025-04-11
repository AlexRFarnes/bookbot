from stats import get_num_words, get_num_chars, get_sorted_chars

def get_book_text(file_path):
    text  = ""
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    return text

def pretty_print(path, word_count, chars_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for dict in chars_count:
        char = dict["char"]
        count = dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

def main():
    path= "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = get_sorted_chars(num_chars)
    pretty_print(path, num_words, sorted_chars)

main()