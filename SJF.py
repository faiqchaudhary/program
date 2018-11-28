process_array = []
n = int(input('Enter the total no of processes: '))
avg_waittime = 0
for j in range(n):
    process_array.append([])
    process_array[j].append(input('Enter name of process: '))
    process_array[j].append(int(input('Enter arrival time of process: ')))
    avg_waittime = avg_waittime + process_array[j][1]
    process_array[j].append(int(input('Enter brust time of process: ')))
    print ('')

    process_array.sort(key = lambda process_array:process_array[2])

print ('ProcessName\tArrivalTime\tBurstTime')
for j in range(n):
    print (process_array[j][0],'\t\t',process_array[j][1],'\t\t',process_array[j][2])
    
print ('Average waiting time: ',(avg_waittime/n))

currentTime = process_array[0][1]
avg_turnarroundtime=0
for i in range(n):
	currentTime = currentTime + process_array[i][2]	
	avg_turnarroundtime = avg_turnarroundtime + currentTime-process_array[i][1]
	print('Turnarount time for ',i,'process is :',(currentTime-process_array[i][1]))

	print('Average Turnaround time : ', avg_turnarroundtime /n)
