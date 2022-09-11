def sumarray(a,cur):
    if cur==len(a)-1:
        return a[cur]
    return a[cur]+sumarray(a,cur+1)


print(sumarray([10,20,30,40],0))