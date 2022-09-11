def print_func(n):
    #print(n)
    if n==0:
        return
    print_func(n-1)
    print(n)
print_func(5)