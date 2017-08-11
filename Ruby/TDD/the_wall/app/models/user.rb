class User < ActiveRecord::Base
    validates :username, presence:true
    validates :username, uniqueness:true
    validates :username, length:{ minimum:5 }
end
