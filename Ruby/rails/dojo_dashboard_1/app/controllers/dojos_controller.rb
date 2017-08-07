class DojosController < ApplicationController
  def index
      @dojos = Dojo.all
    render 'index'
  end

  def new
    render 'new'
  end

  def create
    dojo = Dojo.create(dojo_param)
    if dojo.valid?
      flash[:success] = "Succuessfully created."
      return redirect_to '/'
    else
      flash[:error] = dojo.errors
      redirect_to '/dojos/new'
    end
  end


  private
    def dojo_param
      params.require(:dojo).permit(:branch, :street, :city, :state)
    end
end
