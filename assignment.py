def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)




# Exercise 2
def count_digits(n):
    if n< 10:
        return 1
    return 1 + count_digits(n//10)


# Exercise 3
def sum_digits(n):
    pass
