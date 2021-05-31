import time
init1=time.time()
i=0
while i<45:
    print("Hello")
    i+=1
print(time.time()-init1)
init2=time.time()
for j in range(45):
    print("Hello")
print(time.time()-init2)