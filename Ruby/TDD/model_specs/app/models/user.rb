class User < ActiveRecord::Base
    validates :first_name,:last_name, :email, presence:true
    validates :email, uniqueness: true
    validates :email, format: { with: /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\Z/ }
end
