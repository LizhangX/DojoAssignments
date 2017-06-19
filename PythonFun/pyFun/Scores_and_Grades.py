import random

def ScoresAndGrades(args):
    if args >= 90 :
        print "Score: {}; Your grade is {}".format(args, "A")
    elif args >= 80:
        print "Score: {}; Your grade is {}".format(args, "B")
    elif args >= 70:
        print "Score: {}; Your grade is {}".format(args, "C")
    elif args >= 60:
        print "Score: {}; Your grade is {}".format(args, "D")
    else:
        print "You Failed!"


random_num = random.randint(60,100)
ScoresAndGrades(random_num)
        