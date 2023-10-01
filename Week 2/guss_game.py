import random

n = random.randrange(1,11)
num = int(input("Guss the number from 1 to 10"))

while n!=num:
    if num < n:
        print("Your guss is too low")
        num = int(input("Enter the number again"))
    elif num > n:
        print("Your guss is too high")
        num = int(input("Enter the number again"))
    else:
        break


print("Your guss is correct")