def get_book_text(file):
    
    content = ""

    with open(file) as f:
        content = f.read()
    
    return content

def word_count(text):

    words = text.split()

    return len(words)

def char_count(text):
    chars = {}
    
    text = text.lower()

    for c in text:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1

    return chars

def sort_on(d):
    return d["count"]

def sort_chars(char_dict):
    lst = []

    for c in char_dict:
        if c.isalpha():
            temp = {"char": c, "count": char_dict[c]}
            lst.append(temp)
    
    lst.sort(reverse=True, key=sort_on)

    return lst
