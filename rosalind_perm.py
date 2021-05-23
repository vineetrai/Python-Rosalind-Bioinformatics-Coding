import math
import numpy as np

n = 7
perms = []
ls = [x for x in range(1,n+1)]

def swap(arr, u, v):
    tmp = arr[u]
    arr[u] = arr[v]
    arr[v] = tmp

def heap(size, arr):
    if size == 1:
        tmp = arr.copy()
        perms.append(arr.copy())
        return
    else:
        for idx in range(size):
            heap(size-1, arr)
            if size % 2 == 0:
                swap(arr, 0, size-1)
            else:
                swap(arr, idx, size-1)

heap(n, ls)

f = open("rosalind_perm_out.txt", "w")
f.write(str(len(perms)))
for perm in perms:
    f.write('\n')
    f.write(' '.join(map(str, perm)))
f.close()
    
