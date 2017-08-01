# Challenge: Useful Methods
# Go ahead and try the following methods:
our_hash = {first_name: "Coding", last_name: "Dojo"}
# .delete(key) => deletes and returns a value associated with the key
# e.g.  ruby h = {:first_name => "Coding", :last_name => "Dojo"} h.delete(:last_name) print h # => {:first_name => "Coding"}

a = our_hash.delete(:first_name)
p a

# .empty? => returns true if hash contains no key-value pairs

p our_hash.empty?

# .has_key?(key) => true or false

p our_hash.has_key?(:first_name)

# .has_value?(value) => true or false
p our_hash.has_value?("Dojo")