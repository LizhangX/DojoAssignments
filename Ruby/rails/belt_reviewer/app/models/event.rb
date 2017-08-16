class Event < ActiveRecord::Base
  belongs_to :user, required: true
  has_many :discussions
  has_many :attending_events, dependent: :destroy
  has_many :users, through: :attending_events

  validate :name, :date, :city, :state, presence: true
  validate :date_cannot_be_in_the_past

  def date_cannot_be_in_the_past
    errors.add(:date, "can't be in the past") if !date.blank? and date < Date.today
  end
end
