import sys

def largest_number(a):
    #write your code here
    b = []
    for each in a:
        if len(str(each)) > 1:
            for i in str(each):
                b.append(int(i))
        else:
            b.append(each)
    b.sort(reverse=True)
    s = [str(i) for i in b]
    res = "".join(s)
    res = int(res)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))