#prime number checker


def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("Its a prime number")
    else:
        print("Not Prime!!")


n = int(input("check this number is prime:  "))
prime_checker(n)