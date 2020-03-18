for i in range(9):
    for j in range(9):
        if((i==4)or((j==4 or j==6) and (j+i)%4==0)
        or (j==5 and (j+i)%6==0)
        or(j==7 and (i+j==10 or i+j==12))):
            print("*",end="")
        else:
            print(end=" ")
    print()
