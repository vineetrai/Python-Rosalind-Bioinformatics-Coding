f = open('input.txt', 'r')
linelist = []
i = -1
for line in f:
    i += 1
    if i % 2 == 1:
        linelist += line
f.close()

f = open('output.txt', 'w')
for line in linelist:
    f.write(line)
f.close()
