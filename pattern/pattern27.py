for i in range(0,5):
    for j in range(0,4):
        if(j==0 or ((i==0 or i==2 )and(j!=3)) or (j==3 and i==1)):
           print("*",end="")
        else:
            print(end=" ")
    print()
