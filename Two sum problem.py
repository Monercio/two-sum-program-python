nums = list()
while True:
    input_1 = input('Enter a number (each nuber will be stored only once), once finished, just press enter: ')
    if input_1 == '':
        break
    try:
        if int(input_1) not in nums:
            nums.append(int(input_1))
    except:
        continue
while True:
    input_2 = input('Enter target: ')
    try:
        target = int(input_2)
        break
    except:
        continue
print('given this list', nums)
print('what elements sum the target',target,'?')
lst= list()
d = dict()
#create the list of the reciprocal
for num in nums:
    r = target - num
    lst.append(r)
#print(lst)
# create one single list with reciprocal and original list
tot = nums+lst
#print(tot)
#count equal elements in the total list and put them in dic
for el in tot:
    d[el] = d.get(el,0)+1
#print(d)
fl = list()
# select the keys with value more than one and appends in a list. This list will contain all numbers which in
# specific couples would add up to the target
for k,v in d.items():
    if v > 1:
        #print(k)
        fl.append(k)
#print(fl)
# return the exact couples adding up to the target
for x in fl:
    y = target - x
    if y + x == target and y != x:
        print(x,y)
        print('sum the target')
    else: print('no other couple of numbers sum the target')
