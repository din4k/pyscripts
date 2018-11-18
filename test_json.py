import json
from datetime import datetime

def check_date(dt):
	print ("Inside check date:"+ dt)



now = datetime.now().strftime("%Y-%d-%m")
print(now)

pdir="C:\\Users\\CASPER\\Documents\\dinesh\\ho"
pfile="test.json"
print (pfile)
jsrc=pdir+"\\"+pfile

print (jsrc)
carr =[]
with open (jsrc) as jfile:
	data = json.load(jfile)
	a = tuple(k['dttime'] +">>"+ k['cvalue'] for i in data['record'] for k in i['resource']['cpu'])
	print (a)


'''
with open(jsrc) as jfile:
	data = json.load(jfile)
	for i in data['record']:
		print (i['host_name'])
		for k in i['resource']['cpu']:
			check_date(k['dttime'])
			print (k['dttime'] +">>>>>>"+ k['cvalue'])
			
'''