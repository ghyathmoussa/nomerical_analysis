print('a[0]x^n + a[1]x +....+ a[n]x^0')
n = int(input('Enter the n value: '))
nn = n
A = []
for i in range(0,n+1):
    power = float(input(f'a[{i}] = '))
    A.append(power)
print('f(x) = ')
for x in range(0,n):
    print(f'{A[x]}x^{nn} + ')
    nn-=1
print(str(A[n])+'x^{}'.format(0))
a = float(input('Enter the (a) point: '))
b = float(input('Enter the (b) point: '))
eps = float(input('Enter the epsilon value: '))
count = 0
stop = 0
while stop!=1:
    count+=1
    a1 = 1/a
    b1=1/b
    fa = 0
    fb = 0
    fc = 0
    c = (a+b)/2
    c1 = 1/c
    for i in range(0,n+1):
        a1=a1*a
        fa = fa+A[n-i]*a1
    print(f'f(a)= {fa}')
    for i in range(0,n+1):
        b1 = b1*b
        fb = fb+A[n-i]*b1
    print(f'f(b)= {fb}')
    for i in range(0,n+1):
        c1 = c1*c
        fc=fc+A[n-i]*c1
    print(f'f(c)= {fc}')
    
    if abs(fc)>eps:
        if fa*fc>0:
            a=c
        elif fb*fc>0:
            b=c
    else:
        stop=1
        print(f'The root is {c}')
        print(f'Founded in {count} times')
