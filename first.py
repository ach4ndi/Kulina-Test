
def process(data_array, data_count):
    # limit input by constraits
    if len(data_array) > 100 or int(data_count) > 100:
        print('constraits')
        return

    if not len(data_array) == int(data_count):
        print('data input not same as data count')
        return

    data_pair = []
    pair_count= 0

    for data in data_array:
        if data in data_pair:
            data_pair.remove(data)
            pair_count +=1
        else:
            data_pair.append(data)

    print(pair_count)

data_count = input('')
data_input = input('')

data_array = data_input.split(' ')

process(data_array,data_count)