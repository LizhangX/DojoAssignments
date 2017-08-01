# Print 1-255
# Write a program that would print all the numbers from 1 to 255. 

def print1_255
    (1..255).each{ |i| puts i}
end
print1_255

# Print odd numbers between 1-255
# Write a program that would print all the odd numbers from 1 to 255.
def odd1_255
    (1..255).each{ |i| puts i if i%2 != 0 }
end
odd1_255
# Print Sum
# Write a program that would print the numbers from 0 to 255 but this time, it would also print the sum of the numbers that have been printed so far. For example, your output should be something like this:

# New number: 0 Sum: 0
# New number: 1 Sum: 1
# New number: 2 Sum: 3
# New number: 3 Sum: 6
# ...
# New number: 255 Sum: __
# Do NOT use an array to do this exercise.
def print_sum
    sum = 0
    for i in (1..255) do
        sum += i
        puts "New Number: #{i} Sum: #{sum}"
    end
end
print_sum
# Iterating through an array
# Given an array X, say [1,3,5,7,9,13], write a program that would iterate through each member of the array and print each value on the screen. Being able to loop through each member of the array is extremely important.

arr = [1,2,3,4,5]
def iter(arr)
    arr.each{ |i| puts i }
end
iter(arr)

# Find Max
# Write a program (sets of instructions) that takes any array and prints the maximum value in the array. Your program should also work with a given array that has all negative numbers (e.g. [-3, -5, -7]), or even a mix of positive numbers, negative numbers and zero.

a = [-3, -5 ,-7]
def max(arr)
    max = arr[0]
    for i in arr do
        if i > max
            max = i
        end
    end
    puts max
end
max(a)

# Get Average
# Write a program that takes an array, and prints the AVERAGE of the values in the array. For example for an array [2, 10, 3], your program should print an average of 5. Again, make sure you come up with a simple base case and write instructions to solve that base case first, then test your instructions for other complicated cases. You can use a length function with this assignment.

a = [2,10,3]
def ave(arr)
    sum = 0
    arr.each{ |i| sum += i}
    ave = sum/arr.length
    puts ave
end
ave(a)

# Array with Odd Numbers
# Write a program that creates an array 'y' that contains all the odd numbers between 1 to 255. When the program is done, 'y' should have the value of [1, 3, 5, 7, ... 255].

def odd_arr
    arr = []
    (1..255).each{ |i| arr.push(i) if i%2 != 0 }
    puts arr
end
odd_arr

# Greater Than Y
# Write a program that takes an array and returns the number of values in that array whose value is greater than a given value y. For example, if array = [1, 3, 5, 7] and y = 3, after your program is run it will print 2 (since there are two values in the array that are greater than 3).

a = [1,3,5,7]
y = 3
def greater_than_3(arr, y)
    num = 0
    arr.each{ |i| num += 1 if i > y }
    puts num
end

greater_than_3(a,y)

# Square the values
# Given any array x, say [1, 5, 10, -2], create an algorithm (sets of instructions) that multiplies each value in the array by itself. When the program is done, the array x should have values that have been squared, say [1, 25, 100, 4].

a = [1,5,10,-2]
def square(arr)
    arr.each_index{ |i| arr[i] = arr[i]*arr[i] }
    puts arr
end
square(a)

# Eliminate Negative Numbers
# Given any array x, say [1, 5, 10, -2], create an algorithm that replaces any negative number with the value of 0. When the program is done, x should have no negative values, say [1, 5, 10, 0].

a = [1,5,10,-2]
def eliminate_negative(arr)
    arr.each_index{ |i| arr[i] = 0 if arr[i] < 0 }
    puts arr
end
eliminate_negative(a)

# Max, Min, and Average
# Given any array x, say [1, 5, 10, -2], create an algorithm that returns a hash with the maximum number in the array, the minimum value in the array, and the average of the values in the array.

a = [1,5,10,-2]
def min_max_ave(arr)
    min = max = arr[0]
    sum = 0
    for i in arr do
        sum += i
        if i > max
            max = i
        elsif i < min 
            min = i
        end
    end
    ave = sum/arr.length
    puts "ave: #{ave}, max: #{max}, min: #{min}"
end

min_max_ave(a)

# Shifting the Values in the Array
# Given any array x, say [1, 5, 10, 7, -2], create an algorithm that shifts each number by one to the front. For example, when the program is done, an x of [1, 5, 10, 7, -2] should become [5, 10, 7, -2, 0].

a = [1,5,10,7,-2]
def shift_value(arr)
    arr[arr.length]=0
    arr.shift
    puts arr
end
shift_value(a)

# Number to String
# Write a program that takes an array of numbers and replaces any negative number with the string 'Dojo'. For example, if array x is initially [-1, -3, 2] after your program is done that array should be ['Dojo', 'Dojo', 2].

a = [-1, -3, 2]

def number_to_string(arr)
    arr.each_index{ |i| arr[i] = 'Dojo' if arr[i] < 0 }
    puts arr
end
number_to_string(a)