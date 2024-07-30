def sort_on(dict):
    return dict["num"]

def count_words(book):
    words = book.split()
    return len(words)

def character_count(book):
    characters = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0
        }
    for character in book:
        for ch in characters:
            if character.lower() == ch:
                characters[ch] += 1
    return characters

def creare_character_list(dictionary):
    characters = []
    for char in dictionary:
        ch = {"name" : char, "num" : dictionary[char]}
        characters.append(ch)
    return characters

def print_out(word_count, characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for ch in characters:
        print(f"The {ch['name']} character was found {ch['num']} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    characters = creare_character_list(character_count(file_contents))
    characters.sort(reverse=True, key=sort_on)
    print_out(word_count, characters)
    
main()