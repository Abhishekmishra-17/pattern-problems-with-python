for i in range(0,5):
    for j in range(0,5):
        if((j==0 or j==4)or((j==1 or j==2) and i==j)or(j==3 and i==1)):
             print("*",end="")
        else:
            print(end=" ")
    print()
    
