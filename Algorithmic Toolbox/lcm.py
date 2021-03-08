import sys


def gcd_euclid(a, b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend

def lcm_fast(a, b):
    return (a * b) // gcd_euclid(a, b)

if __name__=='__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))