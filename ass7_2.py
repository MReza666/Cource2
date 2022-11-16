while True:
    fname=input("Enter File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("The file could not be found, please try again")
#
count=0
num=0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count+=1
    words=line.split(":")
    int=float(words[1])
    num+=int
#
ave=num/count
print("Average spam confidence:",ave)
