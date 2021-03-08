import sys


def gcd(a,b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend

if __name__=='__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
