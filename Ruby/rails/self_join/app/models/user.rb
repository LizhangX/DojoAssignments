class User < ActiveRecord::Base
    has_many :who_I_added, through: :user_befriends, source: :user
    has_many :user_befriends, foreign_key:"friend_id", class_name:"Friendship"

    has_many :who_added_me, through: :friend_befriends, source: :friend
    has_many :friend_befriends, foreign_key:"user_id", class_name:"Friendship"

    # has_many :friends, through: :friendships
    # has_many :friendships, foreign_key: :user_id, class_name: :Friendship
    
    # has_and_belongs_to_many :users
end
