import random


def CoinTosses():
    count = 0
    head = 0
    tail = 0
    x = 0
    string = ""
    for i in range(5000):
        x = round(random.random())
        if x == 0.0:
            tail += 1
            string = "tail"
        else:
            head += 1
            string = "head"
        count += 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(count, string, head, tail )
    print "Ending the program, thank you!"

CoinTosses()