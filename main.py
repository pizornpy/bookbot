def main():
    with open(r"/mnt/c/Users/Juan/workspace/github.com/pizornpy/bookbot/books/frankenstein.txt") as f: 
        file_contents = f.read()
    
    amt_words = count_words(file_contents)
    print(file_contents)
    print(amt_words)

def count_words(string):

    return len(string.split())

main()