#4th task
a=input('chess:')
if a[0]=='a' or a[0]=='c' or a[0]=='e' or a[0]=='g':
    if int(a[1])%2==0:
        print('white')
    else:
        print('black')
if  a[0]=='b' or a[0]=='d' or a[0]=='f' or a[0]=='h':
    if int(a[1])%2==1:
        print('white')
    else:
        print('black')