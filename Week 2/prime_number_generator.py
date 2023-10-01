current_number = 2

while True:
    is_prime = True
    for i in range(2, current_number):
        if current_number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Next prime number:", current_number)
    current_number += 1

    user_choice = input("Press 'q' to stop or enter to continue: ")
    if user_choice == 'q':
        break
