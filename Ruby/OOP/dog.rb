require_relative("mammal")

class Dog < Mammal
    def initialize
        super
    end

    def pet
        @health += 5
        return self
    end

    def walk
        @health -= 1
        self
    end

    def run
        @health -= 10
        self
    end
end

dog = Dog.new.walk.walk.walk.run.run.pet.display_health