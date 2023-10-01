n = int(input())
arr = []

for i in range(n):
    number = int(input())
    arr.append(number)

large = arr[0]
second_large = arr[0]
small = arr[0]
second_small = float('inf')

for index in range(n):
    if arr[index] > large:
        large = arr[index]
    
    if arr[index] < small:
        small = arr[index]

for index in range(n):
    if arr[index] > second_large and arr[index] != large:
        second_large = arr[index]
    if arr[index] < second_small and arr[index] != small:
        second_small = arr[index]
    
    

    

print("Second largest element is: ",second_large)
print("Smallest element is: ",small)
print("Seond smallest element is: ",second_small)


