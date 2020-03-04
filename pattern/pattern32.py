for i in range(0,5):
    for j in range(0,5):
        if((j==0 or j==4) and i in range(0,4)) or(i==4 and j in range(1,4)):
           print("*",end="")
        else:
            print(end=" ")
    print()
