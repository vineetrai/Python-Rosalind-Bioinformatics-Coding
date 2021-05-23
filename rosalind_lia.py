import numpy as np
from scipy.stats import binom

def breakup(genotype):
    return [ch for ch in genotype]

def sort(genotype):
    tmp = breakup(genotype)
    tmp.sort(key = str.lower)

    tmp_a = tmp[0:2]
    tmp_b = tmp[2:4]
    tmp_a.sort()
    tmp_b.sort()

    tmp = tmp_a + tmp_b
    return ''.join(tmp)
    
def prob_allele(genotype):
    prob_dict = {
            'AB': genotype.count('A') * genotype.count('B') / 4,
            'Ab': genotype.count('A') * genotype.count('b') / 4,
            'aB': genotype.count('a') * genotype.count('B') / 4,
            'ab': genotype.count('a') * genotype.count('b') / 4
        }
    return prob_dict

def cross(prob_dict):
    pvec = np.asmatrix(list(prob_dict.values()))
    mate = np.matrix([0.25, 0.25, 0.25, 0.25])
    return np.matmul(pvec.T, mate)

def het_prop(mat):
    return sum(np.diag(np.fliplr(mat)))

gtdict = {'AB':0, 'Ab':0, 'aB':0, 'ab':0}
gtarr = np.empty((4,4), dtype = object)
for idx1, el1 in enumerate(gtdict.keys()):
    for idx2, el2 in enumerate(gtdict.keys()):
        gtarr[idx1,idx2] = sort(el1 + el2)

def get_pvec(mat):
    prob_dict = gtdict.copy()
    for i in range(len(gtarr)):
        for j in range(len(gtarr)):
            tmp = prob_allele(gtarr[i,j])
            for k in prob_dict.keys():
                prob_dict[k] += mat[i,j] * tmp[k]
    return prob_dict

def soln(k,n):
    tmp = 'AaBb'
    tmp = prob_allele(tmp)
    for gen in range(k-1):
        tmp = cross(tmp)
        tmp = get_pvec(tmp)
    tmp = cross(tmp)
    tmp = het_prop(tmp)

    pop = 2**k
    part = n-1
    prob = tmp # should always be 0.25
    return 1 - binom.cdf(part, pop, prob)

k = 7
n = 32
tmp = soln(k,n)
print(tmp)
