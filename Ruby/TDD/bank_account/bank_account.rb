class BankAccount
    attr_reader :checking, :saving, :account_number

    @@bank_accounts = 0

    def initialize
        @account_number = generate_account_number
        @checking = 0
        @saving = 0
        @total = 0
        @interest = 0.01
    end

    # def checking_balance
    #     @checking
    # end

    # def saving_balance
    #     p @saving
    #     self
    # end

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
            puts "insufficient funds in checking"
        else
            @checking -= amount
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
        @total = @checking + @saving
    end

    def account_information
        p "Account Number: #{@account_number}, Total money: #{@total}, checking: #{@checking}, saving: #{@saving}, interest rate: #{@interest}"
    end

    private
        def generate_account_number
            return rand(1000000000...10000000000)
        end

end

# account1 = BankAccount.new
# account1.account_information
# account1.deposit_checking(500)
# account1.account_information