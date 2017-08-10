require_relative 'apple_tree'
RSpec.describe AppleTree do
    before(:each) do
        @apple_tree = AppleTree.new
    end
    it "has a age attribute with getter and setter methods" do
        expect(@apple_tree.age).to eq(0)
    end

    it "should have height attribute with only getter method" do
        expect(@apple_tree.height).to eq(1)
        expect{@apple_tree.height = 5}.to raise_error(NoMethodError)
    end

    it "should have height attribute with only getter method" do
        expect(@apple_tree.count).to eq(0)
        expect{@apple_tree.count = 5}.to raise_error(NoMethodError)
    end

    it "should have a method called year_gone_by" do
        @apple_tree.year_gone_by
        expect(@apple_tree.age).to eq(1)
        expect(@apple_tree.height).to eq(1.1)
    end
    
end