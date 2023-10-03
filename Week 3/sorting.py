n = int(input("Enter the size of the array"))
array = []

for i in range(n):
    value = int(input())
    array.append(value)

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] < array[j]:
            array[i],array[j] = array[j],array[i]

        
print(array,end="")