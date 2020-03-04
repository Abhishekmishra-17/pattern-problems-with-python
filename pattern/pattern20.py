for i in range(0,5):
    for j in range(0,3):
        if((i==0 or i==4)or (j==1)):
            print("*",end="")
        else:
            print(end=" ")
    print()
