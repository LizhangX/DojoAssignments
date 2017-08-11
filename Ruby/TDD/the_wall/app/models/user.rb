class User < ActiveRecord::Base
    has_many :messages
    validates :username, presence:true
    validates :username, uniqueness:true
    validates :username, length:{ minimum:5 }
end
