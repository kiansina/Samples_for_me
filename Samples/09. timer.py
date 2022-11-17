
# import the time module
import time

# define the countdown func.
A=0
t=10
while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    A+=1
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

print('Fire in the hole!!')
