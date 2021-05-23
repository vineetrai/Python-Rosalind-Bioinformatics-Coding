def sumodd(a, b):
    sum = 0
    for n in range(a, b+1):
        if n % 2 == 1:
            sum += n
    return sum

print(sumodd(4964, 9821))
