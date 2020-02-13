import matplotlib.pyplot as plt
import time

def fib1(n):
    
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fib1(n - 2) + fib1(n - 1))

runtime1 = []
runtime2 = []
runtime3 = []
items = []

for x in range(0, 25):
    start_time = time.time()
    fib1(x)
    runtime1.append(time.time()- start_time)
    print("Execution time for fib1",x,":",time.time()- start_time)


firstValue = 0
secondValue = 1
           
for num in range(0, 25):
    start_time = time.time()
    if(num <= 1):
                Next = num
    else:
                Next = firstValue + secondValue
                firstValue = secondValue
                secondValue = Next
                      
    runtime2.append(time.time()- start_time)
    print("Execution time for fib2",num,":",time.time()- start_time)


def fib3(number): 
	y = 0
	z = 1
	if number == 0: 
		return y 
	elif number == 1: 
		return z 
	else: 
		for i in range(2,number): 
			w = y + z 
			y = z 
			z = w 
		return z 

for x in range(0, 25):
    items.append(x)
    start_time = time.time()
    fib3(x)
    runtime3.append(time.time()- start_time)
    print("Execution time for fib3",x,":",time.time()- start_time)

plt.plot(items, runtime1, label = "Fib1 (Recursive)")
plt.plot(items, runtime2, label = "Fib2 (Iterative)")
plt.plot(items, runtime3, label = "Fib3 (Space Optimization)")
plt.xlabel("Fibonacci Value")
plt.ylabel("Runtime(time/seconds)")
plt.title("Runtime Differences Between Different Methods of Fibonacci")
plt.legend()
plt.show()
 








    
