import numpy as np

print('a[0]x^n + a[1]x +....+ a[n]x^0')
n = int(input('Enter the n value: '))
nn = n
A = []
for i in range(0,n+1):
    power = float(input(f'a[{i}] = '))
    A.append(power)
fx=np.poly1d(A)
print(f'fx = {fx}')
a = float(input('Enter the (a) point: '))
b = float(input('Enter the (b) point: '))
eps = float(input('Enter the epsilon value: '))
count = 0
stop = 0
while stop!=1:
    count+=1
    fa = 0
    fb = 0
    fc = 0
    fa=np.polyval(A,a)
    print(f'f({a})= {fa}')
    fb=np.polyval(A,b)
    print(f'f({b})= {fb}')
    c=(b*fa-a*fb)/(fa-fb)
    c1=1/c
    fc=np.polyval(A,c)
    print(f'f({c})= {fc}')
    if abs(fc)>eps:
        if fa*fc>0:
            a=c
        elif fb*fc>0:
            b=c
    else:
        stop=1
        print(f'The root is {c}')
        print(f'Founded in {count} times')
