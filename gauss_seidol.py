import numpy as np

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
        if j<3:
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
x01 = float(input('Enter the value of x: '))
x02 = float(input('Enter the value of x: '))
x03 = float(input('Enter the value of x: '))
eps = float(input('Enter the epsilon value: '))
print(items)
print(equales)
stop=1
count = 1
prev1=0
prev2=0
prev3=0
x1=(equales[0][0]-items[0][1]*x02-items[0][2]*x03)/items[0][0]
x2=(equales[1][0]-items[1][0]*x01-items[1][2]*x03)/items[1][1]
x3=(equales[2][0]-items[2][0]*x01-items[2][1]*x02)/items[2][2]
if num ==3:
    if(items[0][0]>items[0][1]+items[0][2] or items[1][1]>items[1][0]+items[1][2]) or items[2][2]>items[2][0]+items[2][1]:
        while(stop!=0):
            count+=1
            prev1=x1
            prev2=x2
            prev3=x3
            x1 = (equales[0][0]-(items[0][1]*x2)-(items[0][2]*x3))/items[0][0]
            x2 = (equales[1][0]-(items[1][0]*x1)-(items[1][2]*x3))/items[1][1]
            x3= (equales[2][0]-(items[2][0]*x1)-(items[2][1]*x2))/items[2][2]
            if(abs(x1-prev1)<=eps and abs(x2-prev2)<=eps):
                stop = 0
    else:
        print('Change the order of functions!:)')
print(f'X1 = {prev1}')
print(f'X2 = {prev2}')
print(f'X3 = {prev3}')
print(f'Founded in  {count} times')