def main():
    book_path = input("Enter the path to the book: ")
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_text_report(letter_count, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_letters(text):
    count_letters = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in count_letters:
                count_letters[char_lower] += 1
            else:
                count_letters[char_lower] = 1
    return count_letters


def print_text_report(letter_count, word_count):
    sorted_letters = sorted(letter_count.items())
    print("--- Begin report of books/frankenstein.txt ---")
    total_words = word_count
    print(f"{total_words} words found in the document\n")
    for char, count in sorted_letters:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()
