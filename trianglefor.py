#print('    *\n   ***\n  *****\n *******\n*********')
n=int(input("give a number: "))
for i in range(n):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('* ',end='')  
    print()