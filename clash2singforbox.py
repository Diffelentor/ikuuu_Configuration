rules_clash=["  - DOMAIN","  - DOMAIN-SUFFIX","  - DOMAIN-KEYWORD","  - IP-CIDR","  - PROCESS-NAME","  - GEOIP"]
rules_singforbox=["domain","domain_suffix","domain_keyword","ip_cidr","process_name","geoip"]

# with open("rules_singforbox.txt","w") as fs:
fs=open("rules_singforbox.txt","w", encoding='utf-8')
with open("rules.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        try:
            rule,website,group=line.strip('\n').replace(",no-resolve","").split(",")
            rule=rules_singforbox[rules_clash.index(rule)]
            # print(rule,website,group)
            output='            {\n                "'+rule+'": [\n                    "'+website+'"\n                ],\n                "outbound": "'+group+'"\n            },\n'
            fs.write(output)
        except:
            print("出现问题",line)
fs.close()