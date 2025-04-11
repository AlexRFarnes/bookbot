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

def sort_on(dict):
    return dict["count"]

def get_sorted_chars(chars):
    sorted_chars = []
    for key in chars:
        char = key
        count = chars[key]
        sorted_chars.append({"char": char, "count": count})
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars


