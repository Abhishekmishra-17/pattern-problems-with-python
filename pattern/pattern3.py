for i in range(1,9):
    for j in range(1,3):
        if((i+j)%2==0):
            print("*",end="")
        else:
            print(end=" ")
    print()
