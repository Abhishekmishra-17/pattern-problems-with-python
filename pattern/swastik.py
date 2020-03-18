for i in range(5):
    for j in range(5):
        if(j==2 or i==2 or(i==4 and j in range(2)) or(i==0 and j in range(3,5)) or(j==0 and i in range(2)) or(j==4 and i in range(3,5))):
            print("*",end="")
        else:
            print(end=" ")
    print()
