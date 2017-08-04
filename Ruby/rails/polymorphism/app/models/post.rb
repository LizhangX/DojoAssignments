class Post < ActiveRecord::Base
  has_many :messages, dependent: :destroy
  has_many :comments, as: :commentable

  belongs_to :blog
  validates :title, :content, presence: true
  validates :title, length: { minimum:7 }
end
