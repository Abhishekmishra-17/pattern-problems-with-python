for i in range(0,5):
    for j in range(5):
        if(i+j==max(range(5)) or (i==j)):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
