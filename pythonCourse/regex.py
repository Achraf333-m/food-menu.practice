import re

file = input('enter a file:')
nums_list = []
with open(file) as openFile:
    for line in openFile:
        nums = re.findall('[0-9]+', line)
        if len(nums) != 0:
            nums_list.append(nums)


summed = []
for list in nums_list:
    for number in list:
        summed.append(int(number))
counter = sum(summed)
        
print('Sum of all the number in the file is:' + ' ' + str(counter))
