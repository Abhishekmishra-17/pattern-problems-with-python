for i in range(5):
    for j in range(4):
        if(i==4 or(j==2 and i in range(3)) or (i==0 and j in range(1,2) or(i-2*j==1))):
            print("*",end="")
        else:
            print(end=" ")
    print()
