first = 1
second = 1

times = int(input())

next_term = 0

for i in range(2,times):
    next_term = first + second
    first = second
    second = next_term

if next_term == 0:
    print(first)
else:
    print(next_term)