def dump_buffer(a, b):
    dnadict[a] = b
    b = ''
    return b

def calc_gc(dna):
    ctr = 0
    for base in dna:
        if base == 'G' or base == 'C':
           ctr += 1
    return ctr / len(dna) * 100


f = open('rosalind_gc.txt', 'r')
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

ros_id, highest_gc = None, 0
for idx in dnadict.keys():
    if calc_gc(dnadict[idx]) > highest_gc:
        highest_gc = calc_gc(dnadict[idx])
        ros_id = idx
        
print(ros_id)
print(highest_gc)
