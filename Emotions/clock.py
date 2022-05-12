import time
start = time.monotonic()

i=0

while i<10:

	print("This is the Photo %d\r\n" % (i+1))
	foto = time.monotonic()-start
	print("Time of this capture: ", foto, "\n")
	time.sleep(3)
	i+=1


stop = time.monotonic()

print("The time of the run:", stop - start)
