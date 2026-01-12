# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

def fizz_buzz(num):
    for n in range(1, num+1):
        div_3 = n % 3 == 0
        div_5 = n % 5 == 0
        if (div_3 or div_5) and not(div_3 and div_5):
            print(n)

# Example:
fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

fizz_buzz(33)
# 3
# 5
# 6
# 9
# 10
# 12
# 18
# 20
# 21
# 24
# 25
# 27
# 33

