class UsersController < ApplicationController
  def index
    render json: User.all
  end

  def new
    render "new"
  end

  def show
    render json: User.find(params[:id])
  end

  def edit
    @user = User.find(params[:id])
    render "edit"
  end

  def create
    User.create(name: params[:name])
    redirect_to '/users'
  end

  def total
    num = User.all.count
    render text: "Total count of users is #{num}."
  end
end
