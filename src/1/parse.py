#!/usr/bin/env python3

f = open("input.txt", "r")

inputs = f.read()
f.close()
lists = inputs.split("\n\n")

output = []
for i in lists:
    calories = i.split("\n")
    counter = 0
    for ii in calories:
        try:
            ii = int(ii)
            counter = counter + ii
        except:
            pass
    
    output.append(counter)

output.sort()
print("Part 1:")
print(str(output[-1]))
print("Part 2:")
print(str(output[-1] + output[-2] + output[-3]))

