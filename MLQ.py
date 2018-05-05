inp=input("Enter the No. of Basic Processes:")
print(inp)
inp=int(inp)

sys_pro=[P0,P1,P2]
int_pro=[P4]
batch_pro=[P5,P6]
burst_time=[0]*inp
waiting_time=[0]*inp
turn_arround=[0]*inp
i=0

burst_time[sys_pro]=input("Enter the burst time:") 
burst_time[int_pro]=input("Enter the burst time:") 
burst_time[batch_pro]=input("Enter the burst time:") 
burst_time=int(burst_time)
 
for i in range(inp):
    for j in range(inp-i):
           set_priority={'1':[sys_pro],'2':[int_pro],'3':[batch_pro]}
           if burst_time[sys_pro]>burst_time[int_pro] & burst_time[sys_pro]>burst_time[batch_pro]:
              print(sys_pro)
           elif burst_time[int_pro]<burst_time[sys_pro] & burst_time[int_pro]>burst_time[batch_pro]:
               print(int_pro)
               elif burst_time[sys_pro]==0 & burst_time[int_pro]:
                   print(batch_pro)
                                                   
waiting_time[0]=0
for i in range(inp):
    waiting_time[int_pro]=0
    for j in range(inp-i):
         waiting_time[int_pro]+=burst_time[sys_pro]
         print("Waiting_time",waiting_time[int_pro])
         
 for i in range(inp):
    waiting_time[batch_pro]=0
    for j in range(inp-i):
         waiting_time[batch_pro]+=burst_time[sys_pro]+burst_time[int_pro]
         print("Waiting_time",waiting_time[batch_pro])
         
turn_around[0]=0

for i in range(inp):
         turn_around[int_pro]+=waiting_time[sys_pro]
         print("Turn_around",turn_around[batch_pro])  

for i in range(inp):
         turn_around[batch_pro]+=waiting_time[sys_pro]+burst_time[sys_pro]+waiting_time[int_pro]+burst_time[int_pro]
         print("Turn_around",turn_around[batch_pro])  
  
