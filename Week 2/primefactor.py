number = int(input("Enter a number: "))

print("Prime factor of",number,"are: ")

factor = 2

while factor <= number:
    if number % factor == 0:
        print(factor)
        number = number // factor
    else:
        factor = factor + 1