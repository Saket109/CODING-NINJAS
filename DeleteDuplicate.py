def uniqueChar(s): 
    d = dict()
    for i in s:
        d[i] = d.get(i,0)+1
        if d[i]>1:
            pass
        else:
            print(i,end= "")
    






# Main 
s=input() 
uniqueChar(s)