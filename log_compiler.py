from datetime import datetime

def main():

	with open('temp/log.txt', 'r') as temp:
			logs = temp.readlines() #store each line as list item
			temp.close()

	logs = [log.split('|') for log in logs] #split each line data: [time, key, evennt]


	for log in logs:

		time_str = log[0][2:] #time, omitting first 2 digits of year: yy-mm-dd
		log[0] = datetime.strptime(time_str, "%y-%m-%d %H:%M:%S,%f") #string to time object


	for log in logs:
		print("log: ", type(log))
		print("logs: ", type(logs))
		if logs.index(log) == 0: #flag first event with t=0
			log[0] = int(0)
		elif logs.index(log) == (len(logs)-1): #flag first event with t=-1
			log[0] = int(-1)
		else:
			log[0] = logs[logs.index(log)+1][0] - logs[logs.index(log)][0]
			log[0] = log[0].total_seconds()
			
	print(logs)

	file = open('logs/log.txt', 'w')
	for log in logs: file.write("{}|{}".format(log[0], log[1]))

if __name__ == '__main__':
	main()