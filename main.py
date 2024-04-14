def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    print_report(book_path, word_count, character_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    counts = {}
    alt_text = text.lower()
    for char in alt_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    sorted_counts = []
    for k, v in counts.items():
        if k.isalpha():
            sorted_counts.append({"name": k, "count": v})
    sorted_counts.sort(reverse=True, key=sort_on)

    return sorted_counts

def sort_on(dict):
    return dict["count"]

def print_report(filepath, total_words, character_counts):
    print(f"--- Begin report of {filepath} ---")
    print(f"{total_words} words found in the document")
    print()
    for el in character_counts:
        print(f"The '{el["name"]}' character was found {el["count"]} times")
    print("--- End report ---")

main()