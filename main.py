from math import sqrt
from itertools import count, islice


def prime_test(n):
    """
    Determines if arguments number is a prime number
    """
    if n < 2:
        return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True


def find_prime():
    """
    Finds all prime numbers between a & b and writes them into a file
     """
    print('==========================================================')
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    output = input('Enter the name for the file output: ')
    print('Working...')
    prime_list = list()

    for i in range(a, b+1):
        if prime_test(i):
            prime_list.append(str(i) + '\n')
        else:
            continue

    with open(output, 'w') as o:
        for item in prime_list:
            o.write(item)
        o.close()
    print('Done created file : ' + output)
    print('==========================================================')


find_prime()
