import time

print('Rocket Launching')
i = 30
while i > -1:
    print('T-'+str(i))
    i -= 1
    time.sleep(0.1)
print('We have lift off')