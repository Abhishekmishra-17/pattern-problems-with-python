for i in range(5):
    for j in range(4):
        if((j==0 and i in range(1,4))or((j in range(1,4)) and (i==0 or i==4))or(j==3 and(i in range(2,4))) or (i==j==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()
