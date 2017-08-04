class Blog < ActiveRecord::Base
    has_many :posts
    has_many :comments, as: :commentable
    validates :name, :description, presence: true
end
