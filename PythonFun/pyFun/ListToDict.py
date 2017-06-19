
def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) >= len(arr2):
        new_dict = dict(zip(arr1,arr2))
    else:
        new_dict = dict(zip(arr2,arr1))     
  # your code here
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar","test"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas",]

x = make_dict(name, favorite_animal)
y = make_dict(favorite_animal, name)

print x,y