for i in range(16):
    for j in range(15):
        if((j==7 and i in range(0,12) and (i+j)%2!=0)or
           ((j==6 or j==8) and i in range(1,12) and (i+j)%2!=0)
        or((j==5 or j==9) and i in range(2,12) and (i+j)%2!=0) or
           ((j==4 or j==10) and i in range(3,12) and (i+j)%2!=0)
           or ((j==3 or j==11)and i in range(6,12)and (i+j)%2!=0)
        or((j==2 or j==12)and i in range(7,12)and (i+j)%2!=0)or
           ((j==1 or j==13)and i in range(10,12)and (i+j)%2!=0) or
           ((j==4 or j==6 or j==8 or j==10 )and i in range(12,16))):
            print("*",end="")
        else:
            print(end=" ")
    print()
