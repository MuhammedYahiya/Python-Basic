num = int(input("Enter the number to find factorial"))

i=1
fact = 1

while i <= num:
    fact = fact * i
    i = i+1

print(fact)
