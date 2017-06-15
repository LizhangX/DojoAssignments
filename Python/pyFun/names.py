#part 1

def printNames(args):
    for i in args:
        print i["first_name"], i["last_name"]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

printNames(students)
print ""

#part 2

def printNames2(args):
    for keys, items  in args.items():
        # print items
        print keys
        count = 0
        length = 0
        for i in items:
            count += 1
            length = len(i["first_name"]) + len(i["last_name"])
            print "{} - {} {} - {}".format(count, i["first_name"].upper(), i["last_name"].upper(),length)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

printNames2(users)