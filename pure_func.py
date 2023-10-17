# a pure function is a function that does not modify the global data, it does not modify what is out of its sope

global_data = [1, 2, 3, 4, 5, 6, 7]

def notPureFunc (item):
    global_data.append(item)
    return global_data

notPureFunc(8)

print(global_data)

# the global list has changed which means this is not a pure function as it did not keep the integrity of the original data

clone_data = global_data.copy()
def pureFunc(item):
    clone_data.append(item)
    return clone_data

pureFunc(9)

# this is a pure function since it uses a clone of data and keeps the original data intact
print(clone_data)
print(global_data)