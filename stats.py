def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_count = {}
    words = text.lower().split()
    
    for word in words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count