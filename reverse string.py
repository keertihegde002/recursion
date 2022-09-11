def reverse(s,i):
    if i==0:
        print(s[i],end=" ")
        return
    print(s[i],end=" ")
    reverse(s,i-1)
    
reverse("abcd",3)