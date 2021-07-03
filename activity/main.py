from datetime import datetime
import json

with open('../temp/log.txt', 'r') as temp:
		logs = temp.readlines() #store each line as list item
		temp.close()

logs = [log.split('|') for log in logs] #split each line data: [time, key, evennt]
for log in logs: log[1] = log[1].replace("\'", "\"")[:-1]
print(logs)
for log in logs: log[1] = json.loads(log[1])
print(logs)


# for log in logs:

# 	#clean the data
	
# 	log[2] = log[2][:-1] #event: 'r\n' => 'r'

# 	time_str = log[0][2:] #time, omitting first 2 digits of year: yy-mm-dd
# 	time_obj = datetime.strptime(time_str, "%y-%m-%d %H:%M:%S,%f") #string to time object
# 	log[0] = time_obj
# 	log = (log[0], log[1], log[2])

# for log in logs:

# 	if logs.index(log) == 0: #flag first event with t=0
# 		log[0] = int(0)
# 	elif logs.index(log) == (len(logs)-1): #flag first event with t=-1
# 		log[0] = int(-1)
# 	else:
# 		log[0] = logs[logs.index(log)+1][0] - logs[logs.index(log)][0]
# 		log[0] = log[0].total_seconds()
	
# logs = [tuple(log) for log in logs]	

# file = open('../logs/log.txt', 'w')
# for log in logs: file.write("{}\n".format(log))