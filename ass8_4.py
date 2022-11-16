while True:
    fname=input("Enter File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("The file could not be found, please try again")
#
lst=list()
for line in fhandle:
    words=line.split()
    for word in words:
        if not word in lst:
            lst.append(word)
#
lst.sort()
print(lst)
