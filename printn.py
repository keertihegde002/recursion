def print_func(n):
    print(n)
    if n==1:
        return
    print_func(n-1)
    
print_func(5)