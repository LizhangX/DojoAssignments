class User < ActiveRecord::Base
  has_secure_password
  validates :name, :email, :password, presence:true
  validates :email, uniqueness:true
  validates :email, format: { with: /(\A([a-z]*\s*)*\<*([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\>*\Z)/i }
  before_save :downcase_email

  def downcase_email
    self.email.downcase!
  end
end
