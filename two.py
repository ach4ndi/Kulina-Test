data_count = input('')
data_input = input('')

count = 0
level = valleys = 0

for step in data_input.split(' '):
    if step == 'U':
        level += 1
    else:
        level -= 1
    
    # when it level 0 and next step are 'U' then valleys +1
    if level == 0 and step == 'U':
        valleys += 1

print(valleys)