#/usr/bin/env python3
import sys


def primef(n):
    """takes an integer as a command-line argument
    and checks if it is a prime number
    
    Args:
        n (int):  input

    Returns:
        int n: a prime number after checking
    """
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if n % i == 0:
                return int(i)
            if n % (i + 2) == 0:
                return primef(n/(i+2))
    return int(n)


print(primef(int(sys.argv[1])))