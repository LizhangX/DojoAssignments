class Blog < ActiveRecord::Base
    has_many :owners
    has_many :posts
    has_many :owner_users, through: :owners, source: :user
    has_many :post_users, through: :posts, source: :user
    has_many :messages, through: :posts
    validates :name, :description, presence: true
end
