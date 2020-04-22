import numpy as np
import math
A = []
B = []
num = int(input('Enter the number of functions: '))
print('Enter the functions: ')
for i in range(0,num):
    print('fx = a[0]x^n + a[1]x +....+ a[n]x^0')
    n=int(input('Enter the n number: '))
    for j in range(0,n+1):
        if j<3:
            item = int(input(f'a[{j}] = '))
            A.append(item)
        else:
            item = int(input(f'c{i+1} = '))
            B.append(item)
items = np.array(A).reshape(3,3)
equales = np.array(B).reshape(3,1)
print(items)
print(equales)
if num == 3:
    det = np.linalg.det(items)
    if det<0:
        det = math.floor(det)
    else:
        det=math.ceil(det)
    # det = items[0][0]*((item[1][1]*items[2][2])-(items[1][2]*items[2][1]))
else:
    print('the number of function should be 3')
for i in range(0,num):
    for j in range(0,num):
        items[j][i] = equales[j][0]
    det1 = np.linalg.det(items)
    x = det1/det
    print(f'x{i+1} = {x}')
    items = np.array(A).reshape(3,3)
