file = open('dragon.txt', 'w') 
'1 = right, 0 = left'
dragonCurve = [1]
output = ''

//dragon curve is defined by turning right, and repeating the previous steps in reverse order and in opposite direction

while len(dragonCurve) < 999999:
    temp1 = dragonCurve
    temp1.reverse()
    temp2 = []
    for x in temp1:
        if x == 1:
            temp2.append(0)
        elif x == 0:
            temp2.append(1)
    temp1.reverse()
    dragonCurve.append(1)
    dragonCurve.extend(temp2)

for x in dragonCurve:
    output += str(x)

file.write(output)
file.close()
