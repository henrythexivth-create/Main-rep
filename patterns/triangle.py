print('this is a right triangle')
n = int(input('enter a number: '))
for i in range (0, n+1):
    for j in range (0, i):
        print('*',end='')
    print()