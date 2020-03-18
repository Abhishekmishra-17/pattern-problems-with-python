for i in range(5):
    for j in range(5):
        if(i==3 or j==3 or(i+j)==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
