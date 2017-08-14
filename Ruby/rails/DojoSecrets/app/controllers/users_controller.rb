class UsersController < ApplicationController
  def index
    @user = User.find(params[:id])
  end

  def new
  end

  def create
    user = User.create(user_param)
    if user.valid?
      return redirect_to '/sessions/new'
    else
      flash[:errors] = user.errors.full_messages
      return redirect_to :back
    end
  end 

  def show
  end

  def edit
  end

  private
    def user_param
      params.require(:user).permit(:name, :email, :password, :password_confirmation)
    end

end
