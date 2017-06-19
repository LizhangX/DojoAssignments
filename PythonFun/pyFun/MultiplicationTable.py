string = ""
for item in range(1,13):
    string = string + " " + str(item) 
print "x", string


for i in range(1,13):
    k = ""
    for j in range(1,13):
        if (i*j) / 1 != 0 and (i*j) / 10 == 0:
            k = k + " " + "  " + " " + str(i*j)
        elif i*j / 10 != 0 and i*j / 100 == 0 :
            k = k + "   " + str(i*j)
        elif i*j / 100 != 0:
            k = k + "  " + str(i*j)
    print i, k


numbers = ""

numbers = "{0: <5}".format("5000")
print numbers