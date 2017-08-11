class UsersController < ApplicationController
  def new
    session[:user_id] ||= 0
    # if session[:user_id] != 0
    #   redirect_to messages_path
    # end
  end

  def create
    user = User.create(user_param)
    unless user.valid?
      flash[:errors] = user.errors.full_messages
      return redirect_to new_user_path
    else
      user = user_param
      @user = User.find_by("username= ?", user[:username])
      p @user
      session[:user_id] = @user.id
      flash[:welcome] = "Welcome, #{@user.username}"
      return redirect_to messages_path
    end
  end

  private
    def user_param
      params.require(:user).permit(:username)
    end
end
