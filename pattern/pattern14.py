for i in range(0,5):
    for j in range(0,4):
        if((j==0 and i in range(1,4))or((j in range(1,4)) and (i==0 or i==4))):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
