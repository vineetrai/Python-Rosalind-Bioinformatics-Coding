aminoacids =    'ARNDCQEGHILKMFPSTWYV'
numcodons =     '46222224236212464124'
stop = 3

relation = {}
for ch in aminoacids:
    idx = aminoacids.find(ch)
    relation[ch] = int(numcodons[idx])

prot = 'MRMHWKLMSPRIRFPVTEKWFIQYNMAEVNMWKGKYDKNWAIIQQDISNKKVTTCMQDGLYLLEQYTNYPESNHTANKYITYPDMNRAIHYYMSWDAYDDPCLHALKPYEQPKWYSDWDAIYGQCFYVMRPQKVHSLTLYAYDQVHFSTFRRYWIMNVFTHLMVPARWPKQSSFLTNSKLRAIKLFTGTLWQLERSTEAIQREDFEWMFRQLKPLRSYPMESIISQHCIWENIPHMYPDSRNFMQNDPMHGYICMMAPHPQSSSRCKAMRRAARGYCQMDYTCWNRWCDMSHMYCSENVWVTPCLIDLVQFTKTDSNYDQQFDLIHYIFKNCLKCFEKDHDAYIMAMPPDWFHWGQSYPDLGAPVDSADPHKAPFVCGAIIKAICDFNFVEWHDSTCRCMIKQNKNTVVKKYPRQDLQPHFLKGMMSERNSRYDWNNYLKAEFENHLIDILCDQRFNIPMDHYKFYGCRQSKRQEEKLWSDPHYCRKGMCGGCFPNMHYHEHRCVFGWEAWDIHYNCATGWWANHHNYNCFPNYSTWCFVPDMVPWAATWAATFDTPCKWAKNFKEKCMGVFYDELVLYRGLAGDTYRYVFWGSFVPMIYGHMNYWHTFHVSLEGFKGNIDLEMEGAEPVVGFTLWLSANFWEFFMTRLSGICIFSTQEKPPWNDQPFNEVKITAYPLPGRTADEYCADKKMQFIGWQWCQVGRGWSDNSWIQARTNMECKGLKPFPEHSSYNDQTYLGEHWTQVINVVGESENNHTVFRCYDPYMPGLAANMDDQCEFLVYPTKKSRESVPTYYPQCTNNKMASMVEVARQSEWQEHCYSADPRSPAFCFRARKVSKTDKHMLFCWTVFVDISPPKEVNRLSNGSAERKWVTGPQCIRFFKGFSPAAFVCAMGELSAHATIGVKTSSVYPFERLFKTWSCKMQWEINYFFRKSSHHFDFVQIQTRCFFIKVQPTYRWQKLIFHIKPVYHVFFVMWVVAGYTCCPFISDLAVQQRPDTCY'

prod = 3
for aa in prot:
    prod *= relation[aa]
    if prod > 1e12:
        prod %= 1e6

answer = int(prod % 1e6)
print(answer)
