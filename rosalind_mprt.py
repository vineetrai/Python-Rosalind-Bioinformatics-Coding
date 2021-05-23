# read input and clean
# for each id in input
    # download FASTA
    # clean
    # check for motifs and store
# write output

import requests
import re

f = open('sample.txt', 'r')
raw = f.readlines()
f.close()

prots = {}
for idx, line in enumerate(raw):
    raw[idx] = line.strip()
    prots[raw[idx]] = None
del(raw)

url_pre = 'http://www.uniprot.org/uniprot/'
url_post = '.fasta'

def dl_FASTA(key):
    url = url_pre + key + url_post
    f = requests.get(url)
    raw = f.text.split('\n')
    raw.pop(0)
    raw.remove('')
    return ''.join(raw)

def find_NG(seq):
    ls = []
    pattern = 'N[^P][ST][^P]'
    for match in re.finditer(pattern, seq):
        ls.append(match.start()+1)
    return ls

for key in prots:
    prot_seq = dl_FASTA(key)
    prots[key] = find_NG(prot_seq)

f = open("output.txt", "w")
for key in prots:
    f.write(key)
    f.write(' '.join(map(str, prots[key])))
f.close()
