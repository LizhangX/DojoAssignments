class EventsController < ApplicationController
  def edit
  end

  def index
    @events_same = Event.where(state: current_user.state) 
    @events_other = Event.where.not(state: current_user.state) 
  end

  def create
    event = Event.new(event_params)
    event.user = current_user
    unless event.save
      flash[:errors] = event.errors.full_messages
    end
      return redirect_to :back
  end

  def show
    @event = Event.find(params[:id])
    @discussions = Discussion.where(event: params[:id])    
  end

  def edit
    
  end

  def destroy
    Event.find(params[:id]).destroy
    return redirect_to :back
  end

  private
    def event_params
      params.require(:event).permit(:name, :date, :city, :state)
    end

end
