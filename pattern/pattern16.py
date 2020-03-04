for i in range(0,5):
    for j in range(0,4):
        if(((i==0 or i==4))or(j==0 and (i in range(1,4)))or(j==1 and i+j==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()
