a = 33
b = 5

def fib(n, k):
    young = 1
    old = 0
    prev_old = 0
    month = 1
    print(month, young, old)
    while month < n:
        prev_old = old
        old += young
        young = prev_old * k
        month += 1
        print(month, young, old)
    return young + old

print(fib(a, b))
