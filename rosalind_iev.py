genopairs = ('AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa')

def punnett_square(cross):
    tmp = cross.split('-')
    offspring = [tmp[0][0] + tmp[1][0],
                 tmp[0][0] + tmp[1][1],
                 tmp[0][1] + tmp[1][0],
                 tmp[0][1] + tmp[1][1]]
    return offspring
        
def num_dominant(offspring):
    ctr = 0
    for genotype in offspring:
        if 'A' in genotype:
           ctr += 1
    return ctr

f = open('rosalind_iev.txt', 'r')
raw = f.readline()
f.close
numlist = [int(x) for x in raw.split()]

expectation = []
for pair in genopairs:
    result = punnett_square(pair)
    expectation.append(num_dominant(result)/2)

dom = 0
for i in range(len(expectation)):
    dom += expectation[i]*numlist[i]

print(dom)
