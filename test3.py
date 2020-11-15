import sys

data1 = []


with open(sys.argv[1]) as f:
    for line in f:
        line = line.replace('\\n', '')
        numbers = line.split()
        for i in numbers:
        	data1.append(float(i))

data2 = []

with open(sys.argv[2]) as f:
    for line in f:
        line = line.replace('\\n', '')
        numbers = line.split()
        for i in numbers:
        	data2.append(float(i))

data3 = []

with open(sys.argv[3]) as f:
    for line in f:
        line = line.replace('\\n', '')
        numbers = line.split()
        for i in numbers:
        	data3.append(float(i))

data4 = []

with open(sys.argv[4]) as f:
    for line in f:
        line = line.replace('\\n', '')
        numbers = line.split()
        for i in numbers:
        	data4.append(float(i))


data5 = []

with open(sys.argv[5]) as f:
    for line in f:
        line = line.replace('\\n', '')
        numbers = line.split()
        for i in numbers:
        	data5.append(float(i))

a = data1[0] + data2[0] + data3[0] + data4[0] + data5[0]

i = 0
c = []

while i != 16:
	b = data1[i] + data2[i] + data3[i] + data4[i] + data5[i]
	c.append(int(b))
	i = i+1

max = c[0]
e = 0

for i in range(len(c)):
    if c[i]>max: 
    	max=c[i]
    	e=i
print(e+1)





