def get_book_text(filepath: str) -> str:

    with open(filepath) as f:
        return f.read()


def number_of_words(text_from_book: str) -> int:

    from collections import Counter

    words: list[str] = text_from_book.split()

    counter = Counter(words)

    num_of_words: int = counter.total()

    return num_of_words


def number_of_chars(text_from_book: str) -> dict[str, int]:

    chars = dict[str, int]()

    words: list[str] = text_from_book.split()

    for word in words:

        word = word.lower()

        for char in word:
            
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    return chars


def print_report(book_path: str) -> None:

    print(f"--- Begin report of {book_path} ---")

    file_text: str = get_book_text(book_path)
    num_words: int = number_of_words(file_text)

    print(f"{num_words} found in the document")
    print()

    num_chars: dict[str, int] = number_of_chars(file_text)

    sorted_chars: list[tuple[str, int]] = list(num_chars.items())

    def sort_on(tupl: tuple[str, int]) -> int:
        return tupl[1]
    
    sorted_chars.sort(key=sort_on, reverse=True)

    for tupl in sorted_chars:
        print(f"The \'{tupl[0]}\' character was found {tupl[1]} times")
    
    print("--- End report ---")


def main():

    book_path: str = "books/frankenstein.txt"

    print_report(book_path=book_path)


if __name__ == '__main__':
    main()