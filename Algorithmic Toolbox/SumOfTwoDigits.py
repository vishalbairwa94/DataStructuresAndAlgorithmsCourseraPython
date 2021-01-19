def sum_of_two_digits(first_mnumber, second_number):
    return first_mnumber + second_number

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(sum_of_two_digits(a,b))
