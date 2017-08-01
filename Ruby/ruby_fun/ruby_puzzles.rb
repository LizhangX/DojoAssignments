# Work on the puzzles below. Make your code as clean as possible. Put all of your answers in a single file and upload below.
#  Create an array with the following values: 3,5,1,2,7,9,8,13,25,32. Print the sum of all numbers in the array. Also have the function return an array that only include numbers that are greater than 10 (e.g. when you pass the array above, it should return an array with the values of 13,25,32 - hint: use reject or find_all method)

a = [3,5,1,2,7,9,8,13,25,32]
def func1(arr)
    sum = 0
    arr.each{ |i| sum+=i }
    new_arr = arr.reject{ |i| i <= 10 }
    puts "sum: #{sum}, new_arr: #{new_arr}"
end
func1(a)


#  Create an array with the following values: John, KB, Oliver, Cory, Matthew, Christopher. Shuffle the array and print the name of each person. Have the program also return an array with names that are longer than 5 characters.

a = ["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"]
def func2(arr)
    arr.shuffle!
    new_arr =[] 
    arr.each{ |i| new_arr.push(i) if i.length > 5 }
    puts "arr: #{arr}, new_arr: #{new_arr}"
end
func2(a)

#  Create an array that contains all 26 letters in the alphabet (this array must have 26 values). Shuffle the array and display the last letter of the array. Have it also display the first letter of the array. If the first letter in the array is a vowel, have it display a message.
def func3
    a = []
    ('a'..'z').each{ |i| a.push(i) }
    a.shuffle!
    puts a[0]
    puts a[a.length-1]
    if ['a','e','i','o','u'].include?(a[0])
        puts "first letter is a vowel"
    end
end
func3

#  Generate an array with 10 random numbers between 55-100.

def func4
    a = []
    (55..100).each{ |i| a.push(i) }
    arr = a.sample(10)
    puts arr
end
func4


#  Generate an array with 10 random numbers between 55-100 and have it be sorted (showing the smallest number in the beginning). Display all the numbers in the array. Next, display the minimum value in the array as well as the maximum value

def func5
    a = []
    (55..100).each{ |i| a.push(i) }
    arr = a.sample(10).sort
    puts '----'
    puts arr
    puts "min is #{arr[0]}"
    puts "max is #{arr[arr.length-1]}"
end
func5

#  Create a random string that is 5 characters long (hint: (65+rand(26)).chr returns a random character)

def func6
    str = ''
    for i in (0..4) do
        str += (65+rand(26)).chr
    end
    return str
end
puts func6

#  Generate an array with 10 random strings that are each 5 characters long
def func7
    arr = []
    for i in (0..9) do
        arr.push(func6)
    end
    return arr
end
puts "---"
puts func7