def count_difference(given_list,change_to,index=0,count=0):
    if index==len(change_to):
        print(count)
        return
    
    
    count_difference(given_list,change_to,index+1,count+abs(given_list[index]-change_to[index]))
    
    
count_difference([15,7,3,21,18,9],[11,5,5,18,20,9])