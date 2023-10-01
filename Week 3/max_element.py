n = int(input("Enter the size of the array"))
array = []

for i in range(n):
    value = int(input())
    array.append(value)

max = 0


for i in range(0, n):
    if max < array[i]:
        max = array[i]

print("Largest element in array is: ",max)