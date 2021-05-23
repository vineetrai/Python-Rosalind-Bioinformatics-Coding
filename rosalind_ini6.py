text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
textlist = text.split(' ')
textlist.sort()
textdict = {}
for i in range(0, len(textlist)):
    if i == 0:
        textdict.update({textlist[i]: 1})
    else:
        if textlist[i] == textlist[i-1]:
            textdict[textlist[i]] += 1
        else:
            textdict.update({textlist[i]: 1})

for x in textdict:
    print(x, textdict[x])
