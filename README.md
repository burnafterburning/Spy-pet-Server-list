# Spy-pet-Server-list
A public and FOSS list of all the servers on Discord Compromised by Spy.Pet
# What is this?
On April 18th, 2024 a disclosure by 404 Media made the rounds announcing that roughly 100k public Discord Servers are hosting sleeper-scraper users, the users in question log and save all messages as well as account details including user bio. Hosting them on their site as a service searchable via crypto-backed credit systems.
This repo hosts a json file with all servers affected to better arm and educate users on the dangers of OP Sec on the public web.

## Checking 
In developer tools, extract your current server IDs
```js
let token = (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
guilds = await fetch("/api/users/@me/guilds", {
  headers: {
    authorization: token
  }
}).then(r => r.json())
console.log(guilds.flatMap(g => g.id))
```

copy+paste the list into this python code
```py
# server ID list goes here
myguilds = ...
import json
servers = json.loads(open('out2.json','r').read())
print(f'checking {len(myguilds)} against {len(servers)} listed servers')

for g in myguilds:
    if g in servers: print(g, servers[g])
```

Note that this does not include servers you have left.
