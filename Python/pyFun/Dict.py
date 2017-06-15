

dict1 = {}
def readDict(keys,values):
    dict1[keys] = values
    for key, value in dict1.iteritems():
        print "My {} is {}".format(key, value)
    print "end"

readDict("name", "Lizhang")
readDict("country", "China")
readDict("favorite food", "hot pot")