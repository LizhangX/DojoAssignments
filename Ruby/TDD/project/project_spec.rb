
require_relative 'project'
RSpec.describe Project do
    before(:each) do
        # updated this block to create two projects
        @project1 = Project.new('Project 1', 'description 1', 'Joe')
        # @project2 = Project.new('Project 2', 'description 2', 'Jose')
    end

    it 'has a getter and setter for name attribute' do
        @project1.name = "Changed Name" # this line would fail if our class did not have a setter method
        expect(@project1.name).to eq("Changed Name") # this line would fail if we did not have a getter or if it did not change the name successfully in the previous line.
    end 

    it 'has a getter and setter for owner attribute' do
        @project1.owner = "Changed Owner" # this line would fail if our class did not have a setter method
        expect(@project1.owner).to eq("Changed Owner") # this line would fail if we did not have a getter or if it did not change the name successfully in the previous line.
    end 

    it 'has a method elevator_pitch to explain name and description' do
        expect(@project1.elevator_pitch).to eq("Project 1, description 1")
        # expect(@project2.elevator_pitch).to eq("Project 2, description 2")
    end

    it 'has a method add_tasks to add task' do
        expect(@project1.add_tasks("one")).to eq (@project1)
    end

    it 'has a method add_tasks to add task' do
        expect(@project1.add_tasks("one").add_tasks("two").tasks).to eq (["one","two"])
    end
end 