x = 27
y = 21
z = 16

def dom_prob(k, m, n):
    t = k + m + n
    sum1 = k/t * ((k-1)/(t-1) + m/(t-1) + n/(t-1))
    sum2 = m/t * k/(t-1) + 3/4 * m/t * (m-1)/(t-1) + 1/2 * m/t * n/(t-1)
    sum3 = n/t * k/(t-1) + 1/2 * n/t * m/(t-1)
    print(sum1, sum2, sum3)
    return sum1 + sum2 + sum3

print(dom_prob(x,y,z))
