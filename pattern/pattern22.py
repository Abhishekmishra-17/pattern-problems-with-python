for i in range(0,5):
    for j in range(0,4):
        if(j==0 or((i-j)==1) or((i+j)==3 and i in range(0,2))):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
