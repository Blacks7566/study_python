import re


match = re.finditer("[^A-Za0-z9]","exAmplE123@#gmil.com")

for m in match:

    print(m.start(),"........",m.group())