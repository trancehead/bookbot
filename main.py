print("hello world")
def read_book(file_path):
    print(f"Trying to open the file: {file_path}")
    with open(file_path, 'r') as f:
        print("File opened successfully.")
        contents = f.read()
        print("File read successfully.")
        return contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def main():
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    
    print("First 100 characters of the book:")
    print(book_text[:100])
    
    print("First 20 words of the book:")
    print(book_text.split()[:20])
    
    word_count = count_words(book_text)
    print(f"The book contains {word_count} words.")
    
    char_count = count_characters(book_text)
    print("Character count in the book:")
    print(char_count)

if __name__ == "__main__":
    main()


