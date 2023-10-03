n = int(input("Enter the size of the array: "))
arr = []

for i in range(n):
    element = int(input())
    arr.append(element)

unique = []
for element in arr:
    if element not in unique:
        unique.append(element)
    
print(unique,end="")