from stats import get_num_words, get_num_chars

def get_book_text(file_path):
    text  = ""
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    return text


def main():
    text = get_book_text("./books/frankenstein.txt")

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    num_chars = get_num_chars(text)
    print(num_chars)

main()