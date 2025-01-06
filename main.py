def main():
    with open(r"/mnt/c/Users/Juan/workspace/github.com/pizornpy/bookbot/books/frankenstein.txt") as f: 
        file_contents = f.read()
    
    map = count_chars(file_contents)
    amt_words = count_words(file_contents)
    
    
    print(file_contents)
    print(amt_words)
    print(map)

def count_words(string):

    return len(string.split())

def count_chars(string):

    map = {}

    for e in string: 
        if e in map:
            map[e] += 1 
        else: 
            map[e] = 1
    return map

main()