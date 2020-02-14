import json

f = open('dataf.json')
a = json.load(f)


a[0]["bbox"][0] = a[2]
print a[0]["bbox"][0] 
 
