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
      flash[:success] = "Succuessfully created dojo #{dojo_param[:branch]}."
      return redirect_to '/'
    else
      flash[:error] = dojo.errors
      redirect_to '/dojos/new'
    end
  end

  def show
    @dojo = Dojo.find(params[:dojo_id])
    @students = Dojo.find(params[:dojo_id]).students
    render 'show'
  end

  def edit
    @dojo = Dojo.find(params[:dojo_id])
    render 'edit'
  end

  def update
    dojo = Dojo.find(params[:dojo_id]).update(dojo_param)
    if dojo 
      flash[:success] = "Succuessfully updated dojo #{dojo_param[:branch]}."
      return redirect_to '/'
    else
      flash[:error] = "invalid update for dojo #{dojo_param[:branch]}"
      return redirect_to "/dojos/#{params[:dojo_id]}/edit"
    end
  end

  def destroy
    Dojo.find(params[:dojo_id]).destroy
    return redirect_to "/"
  end

  private
    def dojo_param
      params.require(:dojo).permit(:branch, :street, :city, :state)
    end
end
