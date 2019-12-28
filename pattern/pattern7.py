for i in range(0,7):
    for j in range(0,4):
        if((i-j==0)or(i+j==6)or(j==0 and i%6!=0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
