for i in range(0,5):
    for j in range(0,5):
        if((i==j or i+j==4) and i in range(0,2))or(j==2 and i in range(2,5)):
           print("*",end="")
        else:
            print(end=" ")
    print()
