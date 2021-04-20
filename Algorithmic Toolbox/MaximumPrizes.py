import sys

def optimal_summands(n):
    summands = []
    sum = 0
    diff = 0
    #write your code here
    if (n-1 == 1 or n == 1):
        return [n]

    for i in range(1,n):
        sum = sum + i
        diff = n - sum
        if(diff > i):
            summands.append(i)
        if(diff == 0):
            summands.append(i)
            break
        if(diff <= summands[-1]):
            total = 0
            for i in summands:
                total = total + i
            final = n - total
            summands.append(final)
            break

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')