#1 zadanie.
r, c = input().split()
arr = list()
 
for _ in range(int(r)):
    arr.append(input().split())
 
m = max(e for r in arr for e in r)
 
for i, r in enumerate(arr):
    if m in r:
        print(i, r.index(m))
        break

#2 zadanie
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

#3 zadanie
n = int(input('n = '))
m = int(input('m = '))
 
r = [['.*'[(j + i) % 2] for j in range(m)] for i in range(n)]
 
print(r)

#4
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))   
    
#5
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()    
    
#6
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
 
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))

#7
n,m= map(int,input().split())
nev = []
res =[]
for i in range(1,n*m+1):
    nev.append(str(i))
    if len (nev) == m:
        res.append(nev)
        nev = []
for i,j in enumerate(res):
    if i%2 !=0:
        j = reversed(j)
    print(*j)
