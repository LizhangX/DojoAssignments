class UsersController < ApplicationController
  def index
  end

  def create
    user = User.create(user_params)
    if user.valid?
      session[:user_id] = user.id
      return redirect_to '/events'
    else
      flash[:errors] = user.errors.full_messages
      return redirect_to :back
    end
  end

  def new
  end

  def edit
  end

  private
    def user_params
      params.require(:user).permit(:first_name, :last_name, :email, :password, :city, :state, :password_confirmation)
    end
end
