def maxRobbery(l,index):
    if index>=(len(l)):
        
        return 0
    
    rob=l[index]+maxRobbery(l,index+2)
    notRob=maxRobbery(l,index+1)
    
    return max(rob,notRob)


print(maxRobbery([1,2,3,4,5,6],0))