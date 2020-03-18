for i in  range(5):
    for j in range(4):
        if(i==0 or j==3 or(i==1 and j==0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
