for i in range(0,5):
    for j in range(0,5):
        if((j==0 or j==4) and i in range(0,3)) or(i==3 and (i-j)%2==0)or(i+j==6):
           print("*",end="")
        else:
            print(end=" ")
    print()
