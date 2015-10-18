# Shin Yamagami
# Oct 18th, 2015
# This program check if the number inputted by a user is a prime number or not.

def get_input():
    return int(input('Please enter a positive integer: '))

def is_prime(x):
    if x <= 1:
        print('False')
    else:
        i = 2
        while x > i:
            if x % i == 0:
                print('False')
                break
            else:
                i = i + 1
        else:
            print('True')

def main():
               
    x = get_input()

    is_prime(x)

main()
