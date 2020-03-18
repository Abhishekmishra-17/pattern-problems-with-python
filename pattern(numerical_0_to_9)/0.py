for i in range(5):
    for j in range(4):
        if(((i==0 or i==4)and j in range(1,3))or( (j==0 or j==3 )and i in range(1,4))):
            print("*",end="")
        else:
            print(end=" ")
    print()
