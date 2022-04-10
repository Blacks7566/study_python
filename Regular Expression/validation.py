import re


count = 0

pattern = re.compile("ab")

match=pattern.finditer("abcabcabc")



for m in match:

    count += 1

    print(m.start(),"...",m.end(),"....",m.group())

print("The no of occurences : ",count)