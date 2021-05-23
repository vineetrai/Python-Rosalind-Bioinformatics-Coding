a = 97
b = 19

def fib(n, m):
    young = 1
    old = 0
    prev_old = 0
    month = 1

    queue = [0]*(m-1)
    queue.append(young)
    print(month, young, old)

    while month < n:
        prev_old = old
        old += young
        young = prev_old
        month += 1
        
        queue.append(young)
        kill = queue.pop(0)
        old -= kill

        print(month, young, old)
        
    return young + old

print(fib(a, b))
