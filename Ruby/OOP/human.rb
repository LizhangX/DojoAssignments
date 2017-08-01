class Human
    attr_accessor :health, :stealth, :intelligence, :strength
    def initialize
        @strength = 3
        @intelligence = 3
        @stealth = 3
        @health =100
    end

    def attack(obj)
        if obj.class.ancestors.include?(Human)
            obj.health -= 3
            true
        else
            false
        end
    end

    def display
        p @health
    end
end

# human1 = Human.new
# human2 = Human.new
# puts human1.health
# puts human1.stealth
# human1.attack(human2)
# human2.display