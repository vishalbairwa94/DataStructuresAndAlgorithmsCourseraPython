def max_pair_product(n, numbers):
    max_index1 = -1
    max_index2 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    for j in range(n):
        if j != max_index1 and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j

    print(str(numbers[max_index1]) + " and " + str(numbers[max_index2]))

    return numbers[max_index1] * numbers[max_index2]


if __name__=='__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    print(max_pair_product(n,a))


