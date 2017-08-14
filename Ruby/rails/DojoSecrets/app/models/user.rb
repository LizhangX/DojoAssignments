class User < ActiveRecord::Base
  has_secure_password
  validates :name, :email, :password, :password_confirmation, presence:true
  validates :email, uniqueness:true
  validates :password, confirmation:true
  validates :email, format: { with: /(\A([a-z]*\s*)*\<*([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\>*\Z)/i }
  before_save :downcase_email

  def downcase_email
    self.email.downcase!
  end
end
