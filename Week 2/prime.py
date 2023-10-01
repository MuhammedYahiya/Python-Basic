# num = int(input("Enter a number to find prime"))
# flag = 0

# if num == 1:
#     flag = 1
# else:
#     for i in range(2,num):
#         if num % i ==0:
#             flag = 1


# if flag == 1:
#     print("Its is not a prime")
# else:
#     print("its is a prime")



for num in range(2,101):
    is_prime = True
    for i in range(2,(num//2)):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end = " ")



