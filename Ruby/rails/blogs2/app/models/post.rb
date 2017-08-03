class Post < ActiveRecord::Base
  belongs_to :blog
  belongs_to :user
  has_many :messages
  has_many :post_users, through: :message, source: :user
  validates :title, :content, presence:true
end
