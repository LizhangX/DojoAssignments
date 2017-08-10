class UsersController < ApplicationController
  def new
  end
  
  def create
    @user = User.new(params.require(:user).permit(:first_name, :last_name, :email))
    if @user.save
      flash[:notice] = ['User successfully created']
      return redirect_to user_path(User.last)
    else
      #errors we need to code later
      flash[:notice] = @user.errors.full_messages
      return redirect_to new_user_path
    end
  end

  def show
    user = User.find(params[:id])
    flash[:welcome] = "Welcome, #{user.first_name}"
  end
end
