fname = input("Enter file name: ")
if len(fname) < 1 : fname ="mbox-short.txt"
fh = open(fname)
#fh = open("mbox-short.txt")
count = 0
lst = list()
lstfrom = list()
# lstemail = list()
# lstemail2 = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From"): continue
    if line.startswith("From:"): continue
    count = count + 1
    lstfrom = line.split()
    print(lstfrom[1])
    #lstemail.append(lstfrom[1])
    #print(lstemail)

#for item in lstemail:
    #if item not in lstemail2:
        #lstemail2.append(item)

#print("last email ",lstemail)
print("There were", count, "lines in the file with From as the first word")
