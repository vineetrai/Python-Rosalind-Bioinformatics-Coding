import FASTA

tmp = FASTA.process('rosalind_grph.txt')
adj = []

for key1 in tmp.keys():
    for key2 in tmp.keys():
        if key1 != key2:
            if tmp[key1][-3:] == tmp[key2][0:3]:
                adj.append([key1, key2])

for i in range(len(adj)):
    print(adj[i][0], end=' ')
    print(adj[i][1])
