for i in range(5):
    for j in range(3):
        if((i==0 or i==4 or (j==0 and i in range(3)) or j==2 or i==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()
