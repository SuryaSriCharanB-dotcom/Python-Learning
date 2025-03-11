for i in range (num,0,-1):
    if(i==1):
        print(" "*(num-i)+"*")
    else:    
        print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
for i in range(2,num+1):
    print(" "*(num-i)+"*"+" "*(2*i-3)+"*")