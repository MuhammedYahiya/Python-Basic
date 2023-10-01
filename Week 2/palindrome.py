num = int(input("Enter a number: "))
reverseNum = 0
temp = num
while temp > 0:
    lastDigit = temp % 10
    reverseNum = reverseNum * 10 + lastDigit
    temp = temp // 10


if num == reverseNum:
    print("Its a palindrome")
else:
    print("It's not a palindrome")