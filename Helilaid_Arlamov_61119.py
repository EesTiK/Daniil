#1
a = int(input())
b = int(input())
if a < b:
    print(a)
elif b < a:
    print(b)
else:
    print("Они равны")
    
#2
x = int(input())    
if x > 0:
    print('+')
elif x < 0:
    print('-')
else:
    print(x)
    
#3
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

#4
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
#5
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
    
#6a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
    
#7
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
    
#8
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')    
    
#9
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')   
    
#10
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')  
    
#11
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
    
#12
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

#13
    n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
if x < y:
    print(x)
else:
    print(y)
    
#14
import random
a = random.randint(1,50)
h = int(input('Сколько попыток будет?:'))
g = 0
while h > 0:
    N = int(input('Введи число от 1 до 50:'))
    if N <= 50:
        if N == a:
            print('Ты угадал')
            a = random.randint(1,50)
            g += 1
        elif N < a:
            print('У тебя ставка ниже')
        else:
            print('У тебя ставка выше')
    else:
        print('Вы ввели не корректное чило')
    h += 1
    print('Осталось',h,'попыток')
print('Загаданно было',a)
print('Угадал', g,'раз')
    

    
    
    
    
    
    