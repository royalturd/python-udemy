def make_incrementor(n):
    return lambda x : x + n                  # lambda fn can only have one expression 

f = make_incrementor(69)                     # calling the function having value 69 or n = 69

print(f(1))                                  # here the value of x = 1 