def is_sortedlist(l,i):
    if i>=len(l):
        return True
    if l[i]<l[i-1]:
        return False
    return is_sortedlist(l,i+1)


l=[1,2,3,4,5,6]    
if is_sortedlist(l,1):
    print("yes l is sorterd")
    
else:
    print("Not sorted")
    