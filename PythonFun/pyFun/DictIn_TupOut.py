
def DictToTup(args):
    k = []
    i = []
    for keys, items in args.iteritems():
        k.append(keys)
        i.append(items)
    
    # newTup = {}
    newTup = zip(k,i)
    return newTup

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

x = DictToTup(my_dict)
print x