for i in range(0,5):
    for j in range(0,5):
        if(((i==0 or i==4) and j==2) or((i==1 or i==3) and j%2!=0)or(i==2 and (j==0 or j==4))):
            print("*",end="")
        else:
            print(end=" ")
    print()
