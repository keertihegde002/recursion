def exponent(n,e):
    if e==0:
        return 1
    return n*exponent(n,e-1)

print(exponent(4,4))