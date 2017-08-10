class AppleTree
    attr_accessor :age
    attr_reader :height, :count
    def initialize
        @age = 0
        @height = 1
        @count = 0
    end

    def year_gone_by
        @age += 1
        @height = @height * 1.1 
        if @age > 3 && @age <= 10
            @count += 2
        end
    end

    def pick_apples
        @count = 0
    end

end