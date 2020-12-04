
switchers = []
long_step = 100
long_switch = 100
lamp_on = 0

for a in range(long_switch):
    switchers.append(0)

for step in range(long_step):
    for instep in range(len(switchers)):
        if not (instep+1) % (step+1) == 0:
            continue
        if switchers[instep] == 0:
            switchers[instep] = 1
        else:
            switchers[instep] = 0
    count_lamp = 0
    
    for lampon in switchers:
        count_lamp += lampon
    
    if count_lamp == len(switchers):
        lamp_on +=1

print(lamp_on)