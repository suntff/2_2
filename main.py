print("Введите глубину треугольника")
n = 2**int(input())
ls = [[1 for j in range(1,i+1)] for i in range(1,n+1)]
for i in range(1,n):
    for j in range(1,len(ls[i])//2+len(ls[i])%2):
        ls[i][j] = ls[i-1][j-1]+ls[i-1][j]
        ls[i][len(ls[i])-1-j] = ls[i][j]
for i in range(n):
    for j in range(len(ls[i])//2+len(ls[i])%2):
        if ls[i][j]%2!=0:
            ls[i][j]="*"
        else:
            ls[i][j]=" "
        ls[i][len(ls[i])-1-j] = ls[i][j]
for i in range(n):
    print(*ls[i])

