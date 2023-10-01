n = int(input("Enter the size of the array"))
array = []

for i in range(n):
    value = int(input())
    array.append(value)

uniqueList = []


for num in array:
    if num % 2 !=0 and num not in uniqueList:
        uniqueList.append(num)


print("Size of the array after removal:",len(uniqueList))
    
