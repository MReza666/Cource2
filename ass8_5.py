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
counter=0
for line in fhandle:
    if not line.startswith("From "):
        continue
    wordlist=line.split()
    sender=wordlist[1]
    print(sender)
    counter+=1
#
print("There were", counter, "lines in the file with From as the first word")
