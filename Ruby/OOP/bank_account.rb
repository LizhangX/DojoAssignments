class BankAccount
    def initialize
        @account_number = generate_account_number
        @checking = 0
        @saving = 0
        @total = 0
        p @account_number
    end

    def checking_balance
        p @chekcing
        self
    end

    def saving_balance
        p @saving
        self
    end

    def deposit_checking(amount)
        p @checking += amount
        self
    end

    def deposit_saving(amount)
        p @saving += amount
        self
    end

    def withdraw_checking(amount)
        if amount > @checking
            p "insufficient funds in checking"
        else
            p @chekcing -= amount
        end
        self
    end

    def withdraw_saving(amount)
        if amount > @saving
            p "insufficient funds in saving"
        else
            p @saving -= amount
        end
        self
    end

    def total_money
        p @total = @checking + @saving
    end

    def account_information
        interest = interest_rate
        p "Account Number: #{@account_number}, Total money: #{@total}, checking: #{@checking}, saving: #{@saving}, interest rate: #{interest}"
    end

    private
        def generate_account_number
            return rand(1000000000...10000000000)
        end

        def interest_rate
            interest = 0.01
        end

end

account1 = BankAccount.new
account1.account_information
account1.deposit_checking(500)
account1.account_information