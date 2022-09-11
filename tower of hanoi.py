def towerOfHanoi(n,source,helper,destination):
    if n==1:
        print("Disk  1 moved from "+source+" to "+destination)
        return
    towerOfHanoi(n-1,source,destination,helper)
    print("Disk ",n, "moved from "+source+" to "+destination)
    towerOfHanoi(n-1,helper,source,destination)
    
    
towerOfHanoi(5,"source","helper","destination")