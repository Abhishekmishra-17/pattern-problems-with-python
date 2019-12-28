for i in range(1,7):
    for j in range(1,8):
        if((i==1 and (j-1)%3!=0)or (i==2 and (j-1)%3==0)or(i-j==2)or(i+j==10)):
            print("*",end='')
        else:
           print(end=' ')
    print('')
