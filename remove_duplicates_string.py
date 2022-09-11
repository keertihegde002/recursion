mapp=[False]*26
def removeDup(string,index,newString):
    global mapp
    
    
    if index==len(string):
        print(newString)
        return
        
    cur=ord(string[index])   
    if mapp[cur-ord('a')]==False:
        mapp[cur-ord("a")]=True
        newString+=string[index]
        removeDup(string,index+1,newString)
    else:
        removeDup(string,index+1,newString)
        
removeDup("aaaabbbcccddd",0,"")
        
        