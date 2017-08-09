
class Project
    # your code here
    attr_accessor :name, :description, :owner, :tasks

    def initialize(name, description, owner, tasks=[])
        @name = name
        @description = description
        @owner = owner
        @tasks = tasks
    end

    def elevator_pitch
        "#{@name}, #{@description}"
    end

    def tasks
        @tasks.each{ |i| i }
    end

    def add_tasks task
        @tasks << task
        self
    end

end
# project1 = Project.new("Project 1", "Description 1")
# puts project1.name # => "Project 1"
# project1.elevator_pitch  # => "Project 1, Description 1"