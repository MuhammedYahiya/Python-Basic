n = int(input("Enter a number"))

temp = n
even_sum = 0
odd_sum = 0

while temp > 0:
    check_num = temp % 10
    if check_num%2 == 0:
        even_sum = even_sum + check_num
        
    if check_num%2 != 0:
        odd_sum = odd_sum + check_num
    

    
    temp = temp //10



print(even_sum,odd_sum)