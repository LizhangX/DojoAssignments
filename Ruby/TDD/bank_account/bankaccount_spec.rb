require_relative 'bank_account'
RSpec.describe BankAccount do
    it "has a getter method for retriving the checking account balance" do
        expect(BankAccount.new.checking).to eq(0)
    end

    it "has a getter method that retrieves the total account balance" do
        expect(BankAccount.new.deposit_checking(5).total_money).to eq(5)
    end

    it "has a function that allows the user to withdraw cash" do
        expect(BankAccount.new.deposit_checking(10).withdraw_checking(5).checking).to eq(5)
    end

    it "raises an error if a user tries to withdraw more money than they have in the account" do
        expect{BankAccount.new.deposit_checking(1).withdraw_checking(5)}.to output("1\ninsufficient funds in checking\n").to_stdout
    end

    it "raises an error when the user attempts to retrives the total number of bank accounts" do 
        expect{ BankAccount.new.bank_account }.to raise_error(NoMethodError)
    end

    it "raise an error when the user attempts to set the interest rate" do
        expect{BankAccount.new.interest = 0}.to raise_error(NoMethodError)
    end
end