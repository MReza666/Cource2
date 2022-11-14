while True:
    fname=input("Inseert File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        fname = "mbox-short.txt"
        fhandle = open(fname)
        break
#
counter=dict()
for line in fhandle:
    if not line.startswith("From "):
        continue
    wordlist=line.split()
    sender=wordlist[1]
    counter[sender]=counter.get(sender,0)+1
#
bigword=None
bigcount=None
for word,count in counter.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
#
print(bigword,bigcount)
