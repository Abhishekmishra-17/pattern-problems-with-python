for i in range(0,5):
    for j in range(0,4):
        if((j==1 or j==2)and (i in range(1,4)))or(j==3 and (i==0 or i==4)):
            print(" ",end="")
        else:
            print("*",end="")
    print("")

