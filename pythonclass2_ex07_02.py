# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
textf = 0.0
textvec = 0.0
avg = 0.0
for text in fh:
    if not text.startswith("X-DSPAM-Confidence:") : continue
    count = count+1;
    textf = float(text[text.find(':')+1:len(text)])
    textvec = textvec + textf

avg = textvec/count
print('Average spam confidence:', avg)
