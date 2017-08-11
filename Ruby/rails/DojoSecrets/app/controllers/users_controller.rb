class UsersController < ApplicationController
  def index
    @user = User.find(params[:id])
  end

  def new
  end

  def show
  end

  def edit
  end
end
