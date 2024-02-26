import sys
import time

number = int(sys.argv[1])


for counter in range(number):
    print(counter+1)
    time.sleep(1) # sleep for 1 second