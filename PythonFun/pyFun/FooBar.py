for i in range(100,100000):
    count1 = 0
    count2 = 0
    for j in range(2,i/2):
        if i % j != 0:
            count1 += 1
        elif i % j == 0:
            if i == j * j:
                count2 += 1
    if count1 == i/2 - 2:
        print "Foo"
    elif count2 == 1:
        print "Bar"
    else:
        print "FooBar"
    
    