def print_down(n: int):
    if n == 0:
        return 0
    print(n, end=" ")
    print_down(n - 1)

def sum_odd(n: int):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + sum_odd(n - 1)
    return sum_odd(n - 1)

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    maximum = max_in_list(lst[1:])
    return max(lst[0], maximum)

def count_even(lst):
    if len(lst) == 0:
        return 0
    if lst[0] % 2 == 0:
        return 1 + count_even(lst[1:])
    return count_even(lst[1:])

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print_down(5)
print()
print(sum_odd(7))
print(power(2, 4))
print(max_in_list([3, 8, 2, 15, 6]))
print(count_even([2,5,8,7,6,3,10]))
print(sum_digits(583))