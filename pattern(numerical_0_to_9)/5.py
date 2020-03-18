for i in  range(6):
    for j in range(3):
        if(i==0 or ((i==2 or i==5)and j in range(2))or(j==2 and i in range(3,5))or(i==1 and j==0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
