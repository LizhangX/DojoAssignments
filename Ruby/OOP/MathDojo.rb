class MathDojo
  # your code here

    def initialize
        @sum = 0
    end

    def add(*arg)
        arg.flatten.each{ |i| @sum+=i }
        return self
    end

    def subtract(*arg)
        arg.flatten.each{ |i| @sum-=i }
        return self
    end

    def result
        p @sum
    end
end

# a = MathDojo.new.display(1,[1,2,3])

challenge1 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).result # => 4
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).result # => 23.15