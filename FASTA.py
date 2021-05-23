def process(file):
    f = open(file, 'r')
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
                buffer = dump_buffer(lastid, buffer, dnadict)
            lastid = line
        else:
            buffer += line
    buffer = dump_buffer(lastid, buffer, dnadict)

    return dnadict

def dump_buffer(a, b, c):
    c[a] = b
    b = ''
    return b
