inp=input("Enter the No. of Processes:")
print(inp)
inp=int(inp)
i=0
j=0
temp=0
arrival_time=[0]*inp
burst_time=[0]*inp
waiting_time=[0]*inp
turn_arround=[0]*inp

time_slice=input("Enter the time slice:")
print(time_slice)

for i in range(inp):
    print("P["+str(i+1)+"]")
    arrival_time[i]=input("Enter the arrival time:")
    burst_time[i]=input("Enter the burst time:")             
waiting_time[i]=0
turn_arround[i]=0

burst_time[i]=int(burst_time[i])
time_slice=int(time_slice)

print("\nProcess\t\twaiting_time\t\tTurn_around time")
while inp!=0:
    if burst_time[i]>time_slice:
        burst_time[i]=burst_time[i]-time_slice
        waiting_time[i]=burst_time[i]
        print("P["+str(i+1)+"]")
        temp+=time_slice
        
    elif burst_time[i]<=time_slice & burst_time[i]>0:
        temp+=burst_time[i]
        burst_time[i]=burst_time[i]-burst_time[i]
        inp=inp-1
        
        waiting_time[i]+=temp-arrival_time[i]-burst_time[i]
        turn_arround[i]+=temp-arrival_time[i]
        print("P["+str(i+1)+"]\t\t",waiting_time[i]+"\tt",turn_arround[i])

