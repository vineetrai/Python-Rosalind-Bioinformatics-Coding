import numpy as np

def dump_buffer(a, b):
    dnadict[a] = b
    b = ''
    return b

f = open('rosalind_cons.txt', 'r')
raw = f.readlines()
f.close()

for idx, line in enumerate(raw):
    raw[idx] = line.strip()
    if line[0] == '>':
        raw[idx] = line[1:].strip()

lastid = ''
buffer = ''
dnadict = {}
for line in raw:
    if line[0:8] == 'Rosalind':
        if lastid != '' and buffer != '':
            buffer = dump_buffer(lastid, buffer)
        lastid = line
    else:
        buffer += line
buffer = dump_buffer(lastid, buffer)

dnastrings = list(dnadict.values())
listarr = []
for string in dnastrings:
    listarr.append(list(string))
listarr = np.asarray(listarr)
profile = np.zeros((4,listarr.shape[1]),dtype=np.int8)
for j in range(listarr.shape[1]):
    profile[0,j] = sum(listarr[:,j] == 'A')
    profile[1,j] = sum(listarr[:,j] == 'C')
    profile[2,j] = sum(listarr[:,j] == 'G')
    profile[3,j] = sum(listarr[:,j] == 'T')
basedict = {0:'A',1:'C',2:'G',3:'T'}
maxind = np.argmax(profile, axis=0)
consensus = ''
for ind in list(maxind):
    consensus += basedict[ind]

print(consensus)
for j in range(4):
    print(basedict[j] + ': ' + \
          ' '.join(map(str, (profile[j,:]))), sep = '')
