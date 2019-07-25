#name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)
handle = open('mbox-short.txt')
sdict = dict()
words = list()
email2 = list()
count = 0
mkey = ''
for line in handle:
	line = line.rstrip()
	words = line.split()
	if not 'From' in words: continue
	if 'From:' in words: continue
	email2.append(words[1])
for word in email2:
	if word not in sdict:
		sdict[word]=1
	else:
		sdict[word]+=1
for key in sdict:
	if sdict[key] > count:
		count = sdict[key]
		mkey = key

print(mkey, count)
#print(max(sdict), sdict[max(sdict)])
#print(handle)
