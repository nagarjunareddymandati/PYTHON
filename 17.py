import sys
import string
def process_file(f1):
    with open(f1, 'r') as file:
        data = file.read().replace('\n', '')
    translator = str.maketrans('', '', string.punctuation)
    data = data.translate(translator)
    words = data.split()
    unique_words = set(words)
    for word in sorted(unique_words):
        print(word)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file>")
        sys.exit(1)add 17
    process_file(sys.argv[1])