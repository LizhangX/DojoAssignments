
#part I
# def draw_stars(args):
#     for item in args:
#         string = ""
#         for i in range(item):
#             string += "*"
#         print string

# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x)                

#part II
def draw_stars(args):
    for item in args:
        if type(item) == int:
            string = ""
            for i in range(item):
                string += "*"
            print string
        elif type(item) == str:
            string2 = ""
            for i in range(len(item)):
               string2 += item[0]
            print string2 


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)     

