inp=input("Enter the No. of Processes:")
print(inp)
inp=int(inp)

i=0
j=0
temp=0

aux_tqueue=[0]*inp
arrival_time=[0]*inp
burst_time=[0]*inp
waiting_time=[0]*inp
turn_arround=[0]*inp

io_wait=input("Enter the input/output waiting time:")
print(io_wait)
time_slice=input("Enter the time slice:")
print(time_slice)

for i in range(inp):
    print("P["+str(i+1)+"]")
    arrival_time[i]=input("Enter the arrival time:")
    burst_time[i]=input("Enter the burst time:")             

waiting_time[i]=0
aux_tqueue[i]=0
turn_arround[i]=0

burst_time[i]=int(burst_time[i])
time_slice=int(time_slice)
io_wait=int(io_wait)

print("\nProcess\t\twaiting_time\t\tTurn_around time")

while inp!=0:
    if burst_time[i]>time_slice:
        burst_time[i]=burst_time[i]-time_slice
        aux_tqueue[i]=burst_time[i]
        if io_wait==0:
            burst_time[i]=aux_tqueue[i]
        temp+=time_slice
        
    elif burst_time[i]<=time_slice & burst_time[i]>0 & aux_tqueue[i]==0:
        temp+=burst_time[i]
        burst_time[i]=burst_time[i]-burst_time[i]
        aux_tqueue[i]=0
        inp=inp-1
        
        waiting_time[i]+=temp-arrival_time[i]-burst_time[i]
        turn_arround[i]+=temp-arrival_time[i]
        print("P["+str(i+1)+"]\t\t",waiting_time[i]+"\tt",turn_arround[i])


