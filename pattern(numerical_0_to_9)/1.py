for i in range(5):
    for j in range(3):
        if((j==1 or i==4)or(i==1 and j==0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
