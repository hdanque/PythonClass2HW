fname = input("Enter file name: ")
fh = open(fname)
#fh = open('romeo.txt')
lst = list()
lst2 = []
for line in fh:
    #print(line.rstrip())
    lst += line.split()
#print(sorted(lst))
for item in lst:
    if item not in lst2:
        lst2.append(item)
print(sorted(lst2))
