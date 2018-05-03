inp=input("Enter the No. of Processes:")
print(inp)
inp=int(inp)
i=0
j=0
temp=0
burst_time=[0]*inp
waiting_time=[0]*inp
turn_arround=[0]*inp

while i<inp:
    burst_time=input("Enter the burst time:")
    i=i+1
    
for i in range(inp):
    for j in range(inp-i):
        if burst_time[j]>burst_time[j+1]:
                temp=burst_time[j]
                burst_time[j]=burst_time[j+1]
                burst_time[j+1]=temp
                

waiting_time[0]=0
for i in range(inp):
    waiting_time[i]=0
    for j in range(inp-i):
         waiting_time[i]+=burst_time[j]
        
turn_around[0]=0
for i in range(inp):
         turn_around[i]+=waiting_time[i]+burst_time[i]
         
    
print("burst_time",burst_time[j],burst_time[j+1])                           
 print("waiting_time",waiting_time[i])
 
print("""turn_aaround" ,turn_around[i])     
