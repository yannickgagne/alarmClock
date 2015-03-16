import json, urllib2, random
import config

imgur = "https://api.imgur.com/3/gallery/random/random/1"

req = urllib2.Request(imgur);
req.add_header('Authorization', config.client_id);
res = urllib2.urlopen(req);
data = json.loads(res.read());
count = 0;
goodList = [];

for x in data["data"]:
	count += 1;
	if 'type' in x:
		if (x["type"] == 'image/jpeg') or (x["type"] == 'image/png'):
			#print count,x["id"],x["type"],x["link"];
			#print x["type"];
			goodList.append(count)
			

print goodList
print random.choice(goodList)

