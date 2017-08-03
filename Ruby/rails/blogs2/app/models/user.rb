class User < ActiveRecord::Base
    has_many :messages
    has_many :posts
    has_many :owners
    has_many :own_blogs, through: :owners, source: :blog
    has_many :write_blogs, through: :posts, source: :blog
    has_many :post_messages, through: :messages, source: :post
    validates :first_name, :last_name, :email_address, presence: true
end
