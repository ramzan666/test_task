import sys

data = []	
src = sys.argv[1]
with open(src) as f:
    for line in f:
        data.append(int(line))

max = data[0]
min = data[0]

for i in data:            #макс/мин значения
	if i > max:
		max = i
	if i < min:
		min = i

n = len(data)

for i in range(n):                  #сортировка списка
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp


if n % 2 == 0:						#медиан
    m1 = data[n//2]
    m2 = data[n//2 - 1]
    m = (m1 + m2)/2
else:
    m = data[n//2]



s = 0

for i in range(n):            #среднее
	s = s + data[i];
s = s / n

a = len(data)*91//100         #90 перцентиль
b = ((len(data)*91)%100)/100
a1 = data[a-1]
a2 = data[a]
c = a1 + b*(a2 - a1)

print(f'{c:.{2}f}\n')
print(f'{m:.{2}f}\n') 
print (f'{max:.{2}f}\n')
print (f'{min:.{2}f}\n')
print(f'{s:.{2}f}\n')