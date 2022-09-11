def print_subset(inpt,output,index):
    if index==len(inpt):
        for i in output:
            print(i,end=" ")
        print()
        return
    
    #exclude part 
    print_subset(inpt,output,index+1)
    
    #include part
    output.append(inpt[index]) 
    print_subset(inpt,output,index+1)
    
print_subset([1,2,3],[],0)
    
    