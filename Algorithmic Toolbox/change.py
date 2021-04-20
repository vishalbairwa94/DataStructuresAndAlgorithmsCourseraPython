import sys

def get_change(m):
    count = 0
    list_deno = [10, 5, 1]
    for i in list_deno:
        remainder = m % i
        req_coins = (m - remainder) / i
        count = count + req_coins
        m = remainder

    m = count

    return int(m)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
