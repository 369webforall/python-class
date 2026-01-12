# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

def reverse_iterate(str):
    for i in range(len(str)-1, -1, -1):
        print(str[i])

# Example:
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b

def reverse_iteratepy(str):
    reverse = str[::-1]
    print(reverse)

reverse_iteratepy("carrot")
reverse_iteratepy("elephant")

    

