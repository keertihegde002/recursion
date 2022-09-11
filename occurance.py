first=-1
last=-1
def FLoccur(string,char,index):
    global first
    global last
    if index==len(string):
        print(first,last)
        return
    
    
    if string[index]==char:
        if first==-1:
            first=index
            
        else:
            last=index
    FLoccur(string,char,index+1)
  

FLoccur("eeiekkeeeerti","i",0)
