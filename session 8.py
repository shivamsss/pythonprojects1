data = [1,2,13,4,5]
print(len(data))
print(max(data))
print(min(data))

print('Simple methods ====================')
def myLen(data):
    length = 0
    for i in data:
        length = length+1
    return length


length = myLen(data)
print(length)


def myMax(data):
    max = data[0]
    for x in data:
        if x > max:
            max = x

    return max


max1 =myMax(data)
print(max1)


def myMin(data):
    min = data[0]
    for x in data:
        if x < min:
            min = x
    return min

min1 = myMin(data)
print(min1)
