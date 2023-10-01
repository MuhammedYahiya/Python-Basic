n = int(input())
arr = []

for i in range(n):
    number = int(input())
    arr.append(number)

large = second_large = float('-inf')
small = second_small = float('inf')

for num in arr:
    if num > large:
        second_large = large
        large = num
    elif num > second_large and num != large:
        second_large = num
    
    if num < small:
        second_small = small
        small = num
    elif num < second_small and num != small:
        second_small = num

print("Second largest element is: ", second_large)
print("Smallest element is: ", small)
print("Second smallest element is: ", second_small)
