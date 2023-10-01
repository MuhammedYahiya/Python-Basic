import math

n = int(input("Enter the size of the array"))
array = []

for i in range(n):
    value = int(input())
    array.append(value)

count = 0

for element in array:
    root = int(math.sqrt(element))
    if root * root == element:
        count += 1

    
print(count)

    