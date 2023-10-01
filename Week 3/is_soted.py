def is_sored(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                return False
        
    return True



n = int(input())
arr = []
for i in range(n):
    number = int(input())
    arr.append(number)

ans = is_sored(arr,n)

if ans:
    print("The given array is sorted")
else:
    print("The given array is not sorted")