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
    time=wordlist[5]
    timelist=time.split(":")
    hour=timelist[0]
    counter[hour]=counter.get(hour,0)+1
#
for k,v in sorted(counter.items()):
    print(k,v)
