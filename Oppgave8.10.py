import random

matrix = []
number = []

for j in range(0, 4):
    number = []
    for i in range(0, 4): 
        number.append(random.randint(0, 1))
    matrix.append(number)

for copy in range(0, 4):
    print(f'{matrix[copy]}')

biggestrow = 0
for f in range(0, 4):
    rowsum = 0
    for z in range(0, 4): 
        rowsum = matrix[f][z]
        if rowsum > biggestrow:
            result = f'1, {z}'

print(f'The biggest row is {result}')

check = 0
bigger = 0
indexNumber = 0
for k in range(0, 4): 
    check = sum(matrix[k])
    if check > bigger: 
        bigger = check
        indexNumber = k

print(f'The largest column index: {indexNumber}')




