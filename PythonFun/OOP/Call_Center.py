
class Call(object):
    def __init__(self, unique_id, name, phone, time, reason):
        # super(Call, self).__init__(*args))
        self.id = unique_id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def display(self):
        print "caller id: {}, caller name: {}, caller phone nubmer: {}, time of call: {}, reason of call: {}.".format(self.id, self.name, self.phone, self.time, self.reason)

call1 = Call(1,"mike",818181,"8:30","blahblahblah")
call1.display()

class CallCenter(object):
    def __init__(self,*args):
        # super(CallCenter, self).__init__(*args)
        self.calls_unsorted = list(args)
        # print self.calls
        self.queue_size = len(args)
        # print self.queue_size
        self.time_list = []
        self.calls = []
        for i in self.calls_unsorted:
            self.time_list.append(i.time)
        self.time_list.sort()
        print self.time_list
        for j in self.time_list:
            for k in self.calls_unsorted:
                if k.time == j:
                    self.calls.append(k)

    def add(self, new_call):
        self.calls.append(new_call)
        return self
    
    def remove(self):
        self.calls.pop(0)
        return self

    def removeByNumber(self,number):
        for i in self.calls:
            if i.phone == number:
                self.calls.remove(i)
        self.queue_size -= 1
        return self
    
    def info(self):
        for i in self.calls:
            print "name: {}, phone number: {}".format(i.name, i.phone)
        print "The length of the queue is: {}".format(self.queue_size)

call2 = Call(2, "Jane", 43434343, "8:40", "no reason")
callcenter1 = CallCenter(call1,call2).info()
callcenter2 = CallCenter(call1,call2).removeByNumber(43434343).info()
callcenter3 = CallCenter(call2,call1).info()