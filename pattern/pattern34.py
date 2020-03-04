for i in range(0,5):
    for j in range(0,5):
        if( i in range(2,5) and (i+j==4 or i==j)) or(j==0 or j==4):
           print("*",end="")
        else:
            print(end=" ")
    print()
