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

while i<inp:
    burst_time=input("Enter the burst time:")
    i=i+1
    
for i in range(inp):
    for j in range(inp-1):
        if arrival_time[j]>arrival_time[j+1]:
                temp=arrival_time[j]
                arrival_time[j]=arrival_time[j+1]
                arrival_time[j+1]=temp
                print("Arrival_time", arrival_time[j], arrival_time[j+1])
                
waiting_time[0]=0
for i in range(inp):
    waiting_time[i]=0
    for j in range(i):
         waiting_time[i]+=burst_time[j]
         print("Waiting_time",waiting_time[i])
         
turn_around[0]=0
for i in range(inp):
         turn_around[i]+=waiting_time[i]+burst_time[i]
         print("Turn_around",turn_around[i])
    
                           
