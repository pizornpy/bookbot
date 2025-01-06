def main():
    with open(r"/mnt/c/Users/Juan/workspace/github.com/pizornpy/bookbot/books/frankenstein.txt") as f: 
        file_contents = f.read()
    
    map = count_chars(file_contents)
    amt_words = count_words(file_contents)
    
    
    print(file_contents)
    print(amt_words)
    print(map)

    print_hashmap(map)

def count_words(string):

    return len(string.split())

def count_chars(string):

    map = {}

    for e in string.lower(): 
        if e in map:
            map[e] += 1 
        else: 
            map[e] = 1
    return map

def print_hashmap(map):
    # Sort the dictionary by value in descending order
    sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)
    
    # Print the sorted map
    for k, v in sorted_map:
        print(f"The character {k} was found {v} times")

main()