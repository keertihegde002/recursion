def print_sum(cur,num):
    if cur==num:
        return num
    return cur+print_sum(cur+1,num)

print(print_sum(1,5))