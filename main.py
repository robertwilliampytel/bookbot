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


def main():

    book_path: str = "books/frankenstein.txt"
    file_text: str = get_book_text(book_path)
    num_words: int = number_of_words(file_text)
    num_chars: dict[str, int] = number_of_chars(file_text)

    print(num_words)
    print(num_chars)


if __name__ == '__main__':
    main()