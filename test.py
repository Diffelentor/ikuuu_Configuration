rules_singforbox={"domain":[],"domain_suffix":[],"domain_keyword":[],"ip_cidr":[],"process_name":[],"geoip":[]}

fs=open("test_revise.txt","w", encoding='utf-8')

with open("test.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    i=0
    while i <len(data):
        # print(data[i])
        for j in rules_singforbox.keys():
            if '"'+j+'"' in data[i]:
                rules_singforbox[j].append(data[i+1])
                i+=6
                break
        i+=1
        # print(rules_singforbox)
# print(rules_singforbox)
for i in rules_singforbox.keys():
    fs.write('                "{}": [\n'.format(i))
    for j in rules_singforbox[i]:
        fs.write(j)
    fs.write('                ],\n')
fs.close()