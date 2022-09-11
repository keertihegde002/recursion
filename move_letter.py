def move(string,char,index,news,count):
    if index==len(string):
        for i in range(count):
            news+=char
        print(news)
        return
    cur=string[index]
    if cur==char:
        count+=1
        move(string,char,index+1,news,count)
    else:
        news+=cur
        move(string,char,index+1,news,count)
        
move("keerti","e",0,"",0)