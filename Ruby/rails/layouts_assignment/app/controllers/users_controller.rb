class UsersController < ApplicationController

  layout "two_column", only: [:index]

  def index
    @users = User.all
  end

  def create
    User.create(user_param)
    return redirect_to '/'
  end

  private
    def user_param
      params.require(:user).permit(:first_name, :last_name, :favorite_language)
    end
end
