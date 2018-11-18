#import requests
import pandas as pd
#import urllib.request
from bs4 import BeautifulSoup
from tabulate import tabulate

wf = open('pref-data.txt','w')
content =""
with open('C:/Program Files (x86)/Hitachi/jp1pcWebCon/Reports/User-PC/User-PC_06082018_CPU_test.htm','r') as f:
	content = (''.join(f.readlines()))


soup = BeautifulSoup(content,'html.parser')
title = soup.title
print(title)
try:
	#table = soup.find_all('table')
	for row in soup.find_all('tr')[2:]:
			for d in row.find_all('td'):
				k = d.find_next('table')
				for tr in k.find_all('tr'):
					#for th in tr.find_all('th'):
						#print(th.text)
						#wf.write(th.text.strip() + "\t")
					#wf.write('\n')	
					for td in tr.find_all('td'):
						#print(td.text)
						wf.write(td.text.strip() + "\t")
					wf.write('\n')
				## to print the output in a tabular from
				#df = pd.read_html(str(k))
				#print( tabulate(df[0], headers='keys', tablefmt='psql'))
except:
	pass
wf.close()
dictd = {}
with open('pref-data.txt', 'r') as rf:
	lines = rf.readlines()
	for i in lines:
		arr = (i.strip()).split('\t')
		dictd[arr[0]]= tuple(val.strip() for val in arr[3:4])
		
print(dictd)
	

			
		

