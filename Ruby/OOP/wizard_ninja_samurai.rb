require_relative("human")

class Wizard < Human
    def initialize
        super
        @health = 50
        @intelligence = 25
    end

    def heal
        @health += 10
    end

    def fire_ball(obj)
        if obj.class.ancestors.include?(Human)
            obj.health -= 20
            true
        else
            false
        end
    end
end

class Ninja < Human
    def initialize
        super
        @health = 175
    end

    def steal(obj)
        if obj.class.ancestors.include?(Human)
            @health += 10
            true
        else
            false
        end
    end

    def get_away
        @health -= 15
    end
end

class Samurai < Human
    @@num = 0
    def initialize
        super
        @health = 200
        @@num += 1
    end

    def death_below(obj)
        if obj.class.ancestors.include?(Human)
            obj.health = 0
            true
        else
            false
        end
    end

    def meditate
        @health = 200
    end

    def how_many
        p @num
    end
end
