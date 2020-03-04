for i in range(0,5):
    for j in range(0,5):
        if((i+j==4)or(i==0 or i==4)):
           print("*",end="")
        else:
            print(end=" ")
    print()
