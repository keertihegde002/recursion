from re import sub
from tokenize import String


def subsequence(string,index,newString):
    if index==len(string):
        print(newString,index)
        return
    #print(newString,"index:",index)
    print("Before calling include",newString,index)
    subsequence(string,index+1,newString+string[index])
    #print(newString,"index:",index)
    #if not included
    print("after calling include string:",newString,"index:",index)
    subsequence(string,index+1,newString)
    #print(newString,"index:",index)+
    
subsequence("abc",0,"")