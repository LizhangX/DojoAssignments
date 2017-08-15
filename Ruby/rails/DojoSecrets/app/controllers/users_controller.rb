class UsersController < ApplicationController
  def index
    @user = User.find(params[:id])
    @secrets = Secret.all 
    # p @user  
    # p @secrets
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
    @user = User.find(params[:id])
  end

  def update
    @user = User.update(params[:id], user_param)
    # p @user.errors.full_messages
    unless @user.valid?
      flash[:errors] = "Email is invalid"
      return redirect_to :back    
    else
      return redirect_to "/users/#{@user.id}"
    end
  end

  def destroy
    User.find(params[:id]).destroy!
    session[:user_id] = nil
    return redirect_to '/users/new'
  end

  private
    def user_param
      params.require(:user).permit(:name, :email, :password, :password_confirmation)
    end
end
