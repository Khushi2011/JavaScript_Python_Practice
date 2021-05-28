# time.time():
# It returns us the seconds of time that have elapsed since the Unix epoch. In simple words,
# it tells us the time in seconds that have passed since 1 January 1970.

# Time.sleep():
# it delays the execution of further commands for given specific seconds.

# The time.localtime()
# is used to convert the number of seconds to local time.
# This function takes seconds as a parameter and returns the date and time in time.struct_time format.
# It is optional to pass seconds as a parameter. If seconds is not provided, the current time will be
# returned by time() is used.
# The syntax is:time.localtime([ sec ])

import time
initial_time=time.time()
print(initial_time)
k=0
while(k<70):
    print("The value of k is:-",k)
    # time.sleep(3)
    k+=1
print("Total time taken by while loop is:-",time.time()-initial_time)

initial=time.time()
for i in range(70):
    print("The value of k is:-", k)
print("Total time taken by for loop is:-",time.time()-initial)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
