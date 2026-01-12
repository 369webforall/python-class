
def sum_of_range(n):
    sum = 0 
    for num in range(1, n+1):
        sum = sum + num
    print(sum)

#1 =  sum + num = 0 + 1 = 1 
#2 = 1 + 2 = 3
#3 = 3 + 3 = 6
#4 = 6 + 4 = 10
#5 = 10 + 5 = 15

sum_of_range(5)

sum_of_range(8)
# prints: 15