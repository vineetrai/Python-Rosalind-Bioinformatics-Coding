import re

# Source: https://www.geeksforgeeks.org/dna-protein-python-3/
table = { 
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
}

dna_rel = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

dna_fs = 'GCCAACAGCGATAAAACGGGACTCATCCGCGGTACCGCGCTGCTGAACAAAGCAGTATAACAATATTTCGGCCCATGACAAGTACGTGTGGACTGCTGCGTGCGCATCCCCCTAATATAGACATAGAGTGCCGTACTGTGGTTCCGTTATGTTATGACAGAGACAGAGATAAGTCCGCGTGTGCGACTTCCGCATGACTCTACTATCCATTCCAGCAATCGCTGTGTGTACTCAATCGCGCATGTTTACTAGGGGTGATTAATCCTGTCCATTGGTTGACGAAAAACAGACTTTTCCGCTCAAAGGTTAAGGTCCCTAGTTTCTACAAATGAAGGTGCAGATCAGTAAACTTGTCGCGGACAATCGAAACCAACGATAAGAGGCGTTGATTACCTTCGACGCTGCTGATGGTGGCGAGTACCAGTCTGCTTATATGACTAGTCCTTACGCTATTGTGCCGGTTTGATAGCTATCAAACCGGCACAATAGCGTAAGGACTAGTCATTCCCAGACTCGTTCTTTGAGTTTGATAAATCTTGACCGACCTTTCCAGGTGTAATAGATTGGTTTGGACAACGCTACTCTTACAGGTCATCTTCGACGTTATCCTTCAATCTGGGAACCATCATTCTCCGGACCGTAAACCACGCGGTAAACGTAAATCTGATCCTGGCGTGTCCAGGTCAAATGCCAGGATTGCTCTGTGCTAATTTATTCCTTAGCTTGACTGTTGACGCATGGGCTATAGGGTACGGATGTTTTCGCAATTTATGGCCTAATCTTCAGAACCACTGCCGTAGAGGCGACGCATATCCCTCTGTTCTAGTTCTTTAGCCCAACGTCGGTTACCGTAAAACCAAGCAAGGGGTACCAGTGTGGGACACTGCTTGGGAATTCTCGATGAGGGTAGCTGAAACAATTTACGCGAAGCCAGCCTT'
dna_rc = ''
for ch in dna_fs[::-1]:
    dna_rc += dna_rel[ch]
strands = [dna_fs, dna_rc]

def get_sites(pattern, dna):
    ls = []
    for match in re.finditer(pattern, dna):
        ls.append(match.start())
    return ls

def get_starts(dna):
    pattern = 'ATG'
    return get_sites(pattern, dna)

def get_ends(dna):
    pattern = 'TAA|TGA|TAG'
    return get_sites(pattern, dna)

def translate(dna, i, st, en):
    st0 = [x for x in st if x % 3 == i]
    en0 = [x for x in en if x % 3 == i]

    idxpairs = []
    for start in st0:
        for end in en0:
            if end > start:
                idxpairs.append((start, end))
                break

    protlist = set()
    for a,b in idxpairs:
        dnapart = dna[a:b]
        i, prot = 0, ''
        while i < len(dnapart):
            prot += table[dnapart[i:i+3]]
            i += 3
        protlist.add(prot)
        
    return protlist

candidates = set()
for strand in strands:
    starts = get_starts(strand)
    ends = get_ends(strand)
    for orf in range(0,3):
        tmp = translate(strand, orf, starts, ends)
        candidates.update(tmp)

for val in candidates:
    print(val)
