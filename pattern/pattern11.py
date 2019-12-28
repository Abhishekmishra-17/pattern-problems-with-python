for i in range(0,5):
    for j in range(9):
        if(i+j==max(range(5)) or (j-i==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
