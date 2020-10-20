def fib(n):                     #write fibonacci series upto n
    a, b = 0, 1
    while a < n:
        print(a, end ='')
        a, b = b, a+b
    print()
#fib(69)                        to call the function
def fib2(n):
    result = []                 #prints result in a list
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib69 = fib2(69)        
print(fib69)