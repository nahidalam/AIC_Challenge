#student report

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys, json;
data = json.load(sys.stdin)
res = []
#print(data)
for key in data:
    value = data[key]
    for i in range (0, len(value)):
        #print(value[i]['enrollment'])
        #for j in range (0, len(value[i]['subject'])):
        for sub in value[i]['subject']:
            #print(sub['grade'])
            if sub['grade'] !='F':
                temp = sub['code'] +' '+ sub['grade'] + ' ' + value[i]['enrollment'] + ' ' +value[i]['name']
                res.append(temp)
res.sort()
#print(res)
for item in res:
    print(item)
