# server ID list goes here
myguilds = ...
import json
servers = json.loads(open('out2.json','r').read())
print(f'checking {len(myguilds)} against {len(servers)} listed servers')

for g in myguilds:
    if g in servers: print(g, servers[g])