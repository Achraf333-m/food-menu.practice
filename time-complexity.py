
def findNumber(number) : 
    counter = 0
    for x in range(100) :
        counter += 1
        if x == number :
            print('number found after' + ' ' + str(counter) + ' ' + 'iterations')

print(findNumber(97))

def binaryFindNumber(number):
    counter = 0
    l = 0
    rang = range(100)
    r = len(rang) - 1

    while l <= r:
        mid = (l + r) // 2
        counter += 1
        print(l, mid, r)
        if number > mid:
            l = mid + 1
        elif number > mid:
            r = mid - 1
        else:
            print('found after', counter)
            break

print(binaryFindNumber(97))