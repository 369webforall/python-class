# Write a function `five_multiples_of(n)` that prints the first five multiples of n.
# The function does not return a value, just prints.

# Example:

def five_multiples_of(n):
    for num in range(1, 6):
        print(n * num)

five_multiples_of(7)

# 7
# 14
# 21
# 28
# 35


# sum_up_to.py

# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(num):
    sum = 0
    for n in range(1, num + 1):
        sum += n # sum = sum + n
    print(sum)

# Example:
sum_up_to(4)  #-> 10
sum_up_to(5)  #-> 15
sum_up_to(2)  #-> 3

# no_ohs.py

# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

# Example:
def no_ohs(str):
    for i in range(len(str)):
       if str[i]  != "o":
           print(str[i])

no_ohs("code")
# c
# d
# e

# odd_sum.py

# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

# Example:

def odd_sum(num):
    sum = 0
    for n in range(1, num+1):
        if n % 2 != 0:
            sum += n
    print(sum)


odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
odd_sum(5)  #-> 9   # 1 + 3 + 5

# string_repeater.py

# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

def string_repeater(str, num):
    result = ""
    for i in range(num):
        result = result + str
    return result


# Example:
print(string_repeater("q", 4))  #-> 'qqqq'
print(string_repeater("go", 2)) #-> 'gogo'
print(string_repeater("tac", 3)) #-> 'tactactac'


# product_up_to.py

# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

# Example:

def product_up_to(max):
    product = 1
    for n in range(1, max + 1):
        product = product * n
    print(product)

product_up_to(4) #-> 24
product_up_to(5) #-> 120
product_up_to(7) #-> 5040

#  div_by_either.py

# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num that are divisible by num1 or num2.
# The function does not return a value, just prints.

# Example:

def div_by_either(n1, n2, max):
    for num in range(1, max):
        if num % n1 == 0 or num % n2 == 0:
            print(num)

div_by_either(4, 3, 16)

# 3
# 4
# 6
# 8
# 9
# 12
# 15
