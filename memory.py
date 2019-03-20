import datetime,pprint,os
import json
now = datetime.datetime.now()
time=(now.strftime("%Y-%m-%d %H:%M:%S"))
user=input('What are you doing now :)\n To show (type)-help : ')
dcit=[{
	'tital':user,
	'correct_time':time,
	'hello :)':"Current date and time : "
}]

# pprint.pprint(dcit)
if user == 'help':
	with open('delye_data.json','r')as top:
		create=json.load(top)
		pprint.pprint(create)

elif os.path.exists('delye_data.json'):
	# print(':)')
	with open('delye_data.json','r')as open_file:
		data=json.load(open_file)
		for o in data:
			dcit.append(o)
	with open('delye_data.json','w')as jamp:
		json.dump(dcit,jamp)

else:
	with open('delye_data.json','w+')as send_file:
		json.dump(dcit,send_file)
