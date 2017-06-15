# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

def TypeList(arr):
    string = ""
    sum = 0
    for i in arr:
        if type(i) == str:
            string = string + " " + i 
        elif type(i) == float or type(i) == int:
            sum += i
    
    if string != "" and sum != 0:
        print "\"The array you entered is of mixed type\""
        print "\"String:{}\"".format(string)
        print "\"Sum: {}\"".format(sum)
    elif string != "":
        print "\"The array you entered is of string type\""
        print "\"String:{}\"".format(string)
    elif sum != 0 and type(sum) == int:
        print "\"The array you entered is of integer type\""
        print "\"Sum: {}\"".format(sum)


l = ['magical unicorns',19,'hello',98.98,'world']
m = [2,3,1,7,4,12]
n = ['magical','unicorns']

TypeList(l)        
TypeList(m)        
TypeList(n)        
        
    