print("hello world")
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_counts = {}
    for char in text.lower():
        if char.isalpha():  # Only count alphabetic characters
            if char not in character_counts:
                character_counts[char] = 0
            character_counts[char] += 1
    return character_counts

def print_report(file_path, word_count, character_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char, count in sorted(character_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def main():
    file_path = "books/frankenstein.txt"
    print(f"Trying to open the file: {file_path}")
    try:
        with open(file_path, 'r') as f:
            print("File opened successfully.")
            text = f.read()
            print("File read successfully.")
            print(f"First 100 characters of the book:\n{text[:100]}")
            words = text.split()[:20]
            print(f"First 20 words of the book:\n{words}")
            word_count = count_words(text)
            character_counts = count_characters(text)
            print_report(file_path, word_count, character_counts)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



