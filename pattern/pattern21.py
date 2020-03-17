for i in range(5):
    for j in range(4):
        if(j==2 or(i==4 and j in range(3)) or(i==0 and j in range(1,4))or(i==3 and j==0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
