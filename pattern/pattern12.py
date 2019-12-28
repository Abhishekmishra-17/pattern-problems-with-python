for i in range(0,5):
    for j in range(9):
        if(i+j==max(range(5)) or (j-i==4)or(i==2 and (j==3 or j==4 or j==5))):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
