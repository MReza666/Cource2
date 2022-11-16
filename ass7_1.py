while True:
    fname=input("Enter File Name:")
    try:
        fhandle = open(fname)
        break
    except:
        print("The file could not be found, please try again")
#
txt=fhandle.read()
captxt=txt.upper()
print(captxt.rstrip())
