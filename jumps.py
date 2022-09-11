def jump(n):
    if n==1 or n==0:
        return 1
    if n<0:
        return 0
    return jump(n-1)+jump(n-2)+jump(n-3)


print(jump(4))