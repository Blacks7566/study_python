import re 

match = re.finditer("a{2,3}","aaaadvccdfssfdaadgadas")


for m in match:

    print(m.start(),".....",m.group())