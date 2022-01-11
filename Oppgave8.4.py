matrix = []

for row in range(0, 8):
    s = input(f'Enter employee {row} hours this week with one space between each day: ')
    matrix.append([int(x) for x in s.split()])

hours = []
for i in range(0, len(matrix)):
    sumHours = sum(matrix[i])
    hours.append([sumHours, i])

hours.sort(reverse=True)

for j in range(0, len(hours)):
    print(f'Employee {hours[j][1]} has worked a total of {hours[j][0]}')


    

    
