"""Exercise
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
"""

import json

s_d="sample-data.json"
with open(s_d, "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':60} {'Description':12} {'Speed':8} {'MTU':5}")
print("-" * 80)


for i in data["imdata"]:
    a = i["l1PhysIf"]["attributes"]

    dn = a.get("dn", "")
    dsc = a.get("descr", "")
    speed = a.get("speed", "")
    mtu = a.get("mtu", "")


    print(f"{dn:60} {dsc:12} {speed:8} {mtu:5}")
