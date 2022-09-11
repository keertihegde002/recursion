def print_spelling(n,l):
    if n==0:
        return 
    
    print_spelling(n//10,l)
    
    print(l[n%10])
    
l=["zero","one","two","three","four","five","six","seven","eight","nine"]
print(print_spelling(123,l))
    