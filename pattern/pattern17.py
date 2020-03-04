for i in range(0,5):
    for j in range(0,4):
        if((i==0 or j==0) or (i==2 and ((i-j)==1 or (i-j)==0))):
            print("*",end="")
        else:
            print(end=" ")
    print()
