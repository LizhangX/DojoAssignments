
#odd/even
def oddEven():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)
        elif i % 2 == 1:
            print "Number is {}. This is an odd number.".format(i)

oddEven()


#multiply

def multiply(arr, num):
    newarr = []
    for i in arr:
        newarr.append(i * num)
    return newarr

a = [2,4,10,16]
b = multiply(a, 5)
print b

#Hacker Challenge
def layered_multiples(arr):
    new_array = []
    for i in arr:
        array = []
        for j in range(i):
            array.append(1)
        new_array.append(array)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x