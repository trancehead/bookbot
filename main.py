print("hello world")
def count_words(text):
    """Count the number of words in the given text."""
    words = text.split()  # Split text into words
    return len(words)

def main():
    path_to_file = "books/frankenstein.txt"
    print(f"Trying to open the file: {path_to_file}")
    
    try:
        with open(path_to_file, 'r') as f:
            print("File opened successfully.")
            file_contents = f.read()
            print("File read successfully.")
    except FileNotFoundError:
        print("File not found.")
        return

    # Debug: Print the first 100 characters
    print("First 100 characters of the book:")
    print(file_contents[:100])
    
    # Debug: Print the first 20 words
    words_debug = file_contents.split()[:20]
    print("First 20 words of the book:")
    print(words_debug)
    
    # Exclude Project Gutenberg's boilerplate text
    start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK"
    
    start_index = file_contents.find(start_marker)
    end_index = file_contents.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        file_contents = file_contents[start_index + len(start_marker):end_index]
    
    # Count words
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")

if __name__ == "__main__":
    main()


