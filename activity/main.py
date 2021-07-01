import datetime

temp = open('../temp/log.txt', 'r')

logs = temp.readlines() #store each line as list item

logs = [log.split('|') for log in logs] #split each line data: [time, key, evennt]

for log in logs:

	#clean the data
	log[0] = log[0][2:-4] #time: '2021-07-01 15:11:10,968' => '21-07-01 15:11:10'
	log[2] = log[2][:-1] #event: 'r\n' => 'r'

	time_str = log[0]
	time_obj = datetime.strptime(time_str, "%y-%m-%d %H:%M:%S") #string to time object
	log[0] = time_obj
	log = (log[0], log[1], log[2])
	print(log)
print(logs)

