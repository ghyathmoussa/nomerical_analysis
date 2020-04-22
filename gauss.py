import numpy as np
import math
item=[]
esit=[]
items=[]
equales=[]
num = int(input('Enter the number of functions: '))
print('Enter the functions: ')
for i in range(0,num):
    print('fx = a[0]x^n + a[1]x +....+ a[n]x^0')
    n=int(input('Enter the n number: '))
    for j in range(0,n+1):
        if j<n:
            a = float(input(f'a[{j}] = '))
            item.append(a)
        else:
            b = float(input(f'c{i+1} = '))
            esit.append(b)
    items.append(item)
    equales.append(esit)
    item = []
    esit=[]
items = np.array(items)
equales=np.array(equales)
print(items)
print(equales)
roots = np.linalg.solve(items,equales)
print(roots)
print(f'X1 = {roots[0][0]}')
print(f'X2 = {roots[1][0]}')
print(f'X3 = {roots[2][0]}')
