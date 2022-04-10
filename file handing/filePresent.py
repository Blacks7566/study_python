import os


fname = input("Enter filename to check : ")

if os.path.isfile(fname):

    print("file exist : ",fname)
    f = open(fname,'r')


else:

    print("file dose not exsit : ",fname)
    os._exit(0)

# text = f.read()

# print("content of file is : ",text )



lcount = wcount = ccount = 0

for line in f:
    lcount = lcount+1
    ccount = ccount + len(line)
    words = line.split(" ")

    wcount = wcount+len((words))

print("number of line: ",lcount)
print("number of characters: ",ccount)
print("number of words: ",wcount)
