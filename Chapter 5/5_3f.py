# You can sort the list first then traverse it to print the
# entries of the dictionary in alphatical order

info = {"occupation":"manager", "name":"Sandy"}

theKeys = list(info.keys())
theKeys.sort()

for key in theKeys:
    print(key, info[key])
