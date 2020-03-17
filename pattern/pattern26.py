for i in range(0,5):
    for j in range(0,4):
        if((i in range(1,4) and(j==0 or j==3))or (j in range(1,3) and(i==0 or i==4))):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
