#!/bin/python3

import json

f = open("ipaddress_list.json")

data = json.load(f)

#{'hostname': 'helium.rainsbrook.co.uk', 'ipaddress': '81.187.218.250', 'open_ports': [80, 53, 443]}

for host in data['hosts']:
    print(host['hostname'], host['ipaddress'])
    for port in host['open_ports']:
        print(port)

# Closing file
f.close()

exit
