def main():
    # Retrieve book text as list of strings
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    
    # Get word count and character counts
    w_count = word_count(book_text) # Integer
    c_count = character_count(book_text) # List of dicts
    c_count.sort(reverse=True, key=sort_on) # Sort by count, descending

    print_stats(w_count, c_count, filepath)

def print_stats(word_count, char_count, filepath):
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")

    for c_count in char_count:
        c = c_count["char"]
        count = c_count["count"]

        print(f"the '{c}' character was found {count} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def character_count(book_text):
    char_count = {}
    for word in book_text:
        for c in word.lower():
            if  not c.isalpha():
                continue
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
    
    #Convert single dict to list of dicts
    char_count_list = []
    for c in char_count:
        char_count_list.append({"char":  c, "count": char_count[c]})
    return char_count_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents.split()

def word_count(text):
    return len(text)

main()
