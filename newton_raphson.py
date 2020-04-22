import numpy as np

print('a[0]x^n + a[1]x +....+ a[n]x^0')
n = int(input('Enter the n value: '))
nn = n
A = []
B = []
for i in range(0,n+1):
    power = int(input(f'a[{i}] = '))
    A.append(power)
fx=np.poly1d(A)
print(f'f(x) = {fx}')
# for x in range(0,n):
#     print(f'{A[x]}x^{nn} + ')
#     nn-=1
# print(str(A[n])+'x^{}'.format(0))
x0 = float(input('Enter the x value to found: '))
result = 0
x = 1/x0
stop = 0
count = 0
eps = float(input('Enter the epsilon value: '))
# print("f'(x) = ")
nn=n
for i in range(0,n-1):
    sume = A[i]*nn
    B.append(sume)
    # print('{}x^{} + '.format(B[i],nn-1))
    nn-=1
B.append(A[n-1])
fx1=np.poly1d(B)
print(f"f'(x)={fx1}")
# print(A[n-1])
while stop!=1:
    fx0 = 0
    fx01 = 0
    count+=1
    xk = 0
    x=1/x0
    for i in range(0,n+1):
        x = x*x0
        fx0 = fx0 + A[n-i]*x
    x = 1/x0
    for j in range(0,n):
        x=x*x0
        fx01 = fx01+B[n-j-1]*x
    xk = x0 - fx0/fx01
    if x0-xk>eps or xk-x0>eps:
        x0=xk
    else:
        print(f'Te root is {xk}')
        print(f'Founded in {count} times')
        stop = 1


# print(fx0)

    