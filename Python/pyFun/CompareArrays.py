

def CompareArrays(l1,l2):
    count = 0
    if len(l1) != len(l2):
        print "The lists are not the same."
    else:
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                count += 1
            elif l1[i] != l2[i]:
                
                print "The lists are not the same."
        if count == len(l1):
            print "The lists are the same"


list_1 = [1,2,5,6,2]
list_2 = [1,2,5,6,2]

list_3 = [1,2,5,6,5]
list_4 = [1,2,5,6,5,3]

list_5 = [1,2,5,6,5,16]
list_6 = [1,2,5,6,5]

list_7 = ['celery','carrots','bread','milk']
list_8 = ['celery','carrots','bread','cream']


CompareArrays(list_1,list_2)
CompareArrays(list_3,list_4)
CompareArrays(list_5,list_6)
CompareArrays(list_7,list_8)