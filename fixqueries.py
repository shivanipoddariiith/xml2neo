import os
import re
path = os.getcwd()
os.chdir(path)
f = open('fixme')
fixed = open('fixed','w')
l = ''
def find_match(text, search):
    result = re.findall('\\b'+search+'\\b', text)
    if len(result)>0:
        return True
    else:
        return False
count = 0
count2 = 0
for line in f.readlines():
    nocheck = 0
    flag = 0

    if find_match(line, "CREATE") is True:
        flag = 0
        line = line.rstrip() + ';'
        count = count + 1
        nocheck = 1
    
    if find_match(line, "MATCH") is True:
        line = line.rstrip()
        flag = 0

    if line.rstrip() == ";" and nocheck == 0:
        flag = 1
        count2 = count2+1
    
    if flag is 0:
        fixed.write(line + "\n")

print count
print count2


