def guess_number guess
    number = 25
    # your code here
    if guess == 25
        return "You got it"
    elsif guess > 25
        return "Guess is too high!"
    else
        return "Guess is too low!"
    end
end 

puts guess_number 25
puts guess_number 26
puts guess_number 24