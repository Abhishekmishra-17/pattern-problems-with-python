for i in range(0,9):
    for j in range(0,5):
        if((j==4 and (i+j)%4!=0) or (j==0) or((j==1 or j==2 ) and i%4==0)):
            print("*",end="")
        else:
             print(end=" ")
    print()
