class MessagesController < ApplicationController
  
  def index
    @user = User.find_by(session[:user_id])
    @messages = Message.all
  end

  def create
    message = Message.create(message_param)
    unless message.valid?
      flash[:errors] = message.errors.full_messages
    end
    return redirect_to messages_path
  end

  private
    def message_param
      params.require(:message).permit(:message, :user_id)
    end
end
