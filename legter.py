#!/usr/bin/python
import requests
import os

URL1 = "http://kiri.project.webtown.hu/web/pg/napi-legter"
URL2 = "http://kiri.project.webtown.hu/web/pg/napi-legter?p_p_id=1_WAR_dailyairspaceportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_1_WAR_dailyairspaceportlet_cmd=downloadOA&_1_WAR_dailyairspaceportlet_importTab="
HEADER = {'Authorization' : 'Basic bmFwaWxlZ3RlcjpneW9neWkxMjM='}
key = ""

POST = {'_1_WAR_dailyairspaceportlet_dlTRA' : 'true',
	'_1_WAR_dailyairspaceportlet_dlTRACheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlDA' : 'true',
	'_1_WAR_dailyairspaceportlet_dlDACheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlESETI' : 'true',
	'_1_WAR_dailyairspaceportlet_dlESETICheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlCTRTMA' : 'true',
	'_1_WAR_dailyairspaceportlet_dlCTRTMACheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlP' : 'true',
	'_1_WAR_dailyairspaceportlet_dlPCheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlR' : 'true',
	'_1_WAR_dailyairspaceportlet_dlRCheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlA' : 'true',
	'_1_WAR_dailyairspaceportlet_dlACheckbox' : 'true',
	'_1_WAR_dailyairspaceportlet_dlDROPZONE' : 'true',
	'_1_WAR_dailyairspaceportlet_dlDROPZONECheckbox' : 'true',
	'j_username' : 'napilegter',
	'j_password' : 'gyogyi123'}

r = requests.get(URL1, auth=('napilegter', 'gyogyi123'), headers=HEADER)

for line in r.text.splitlines():
	if not 'importTab=' in line:
		continue
	key = line.split('importTab=')[1].split('"')[0]

r = requests.post(URL2 + key, POST, headers=HEADER)

with open('napi_legter_OA.txt', 'w') as file:
	for line in r.text.splitlines():
		line = line.replace('ft SL', 'ft MSL')
		line = line.replace('feet<br>', 'ft ')
		line = line.replace('<br>', ' ')
		line = line.replace('#REF!', '1500')
		line = line.encode('ascii', 'ignore').decode('ascii')
		file.write(line + '\n')


