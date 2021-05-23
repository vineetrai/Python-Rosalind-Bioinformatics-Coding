import FASTA

tmp = FASTA.process('rosalind_lcsm.txt')
dnalib = list(tmp.values())
dnalib.sort(key = len)

# Longest common substring cannot be longer than shortest DNA string
# Initialize this substring as the best guess for now
bestsub = dnalib[0]

# Create list of all substrings of best substring
slices = []
n = len(bestsub)
ls = []
for i in range(n):
    for j in range(i+1,n+1):
        # print(i,j)
        slices.append(bestsub[i:j])

# Remove duplicates and sort longest to shortest
slices = list(dict.fromkeys(slices))
slices.sort(key = len)
slices.reverse()

i = 0
t = 0
flag = False
while flag is False:
    if slices[t] in dnalib[i]:
        i += 1
    else:
        t += 1
        i = 0
    if i is len(dnalib):
        flag = True

print(slices[t])
