#Write a function that prints all **indexes** where a character appears in a string.

def find_char_positions(str, char):
    for i in range(len(str)):
        if str[i] == char:
            print(i)



find_char_positions("banana", "a")
# 1
# 3
# 5

find_char_positions("omango", "o")

