def find_max(*args):
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value

print(find_max(3, 5, 2, 8, 1))



def multiplication_table(n):
    i = 10
    while i >= 1:
        print(f"{n} * {i} = {n * i}")
        i -= 1

multiplication_table(5)
