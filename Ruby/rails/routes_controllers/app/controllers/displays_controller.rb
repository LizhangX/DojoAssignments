class DisplaysController < ApplicationController
  def index
    render text: "What do you want me to say???"    
  end

  def hello
    render text: "Hello CodingDojo"
  end

  def say_hello
    @id = params[:id] || ''
    if @id == 'michael'
      @id = 'joe'
    end
    render text: "Saying Hello #{@id}!"
  end

  def times
    session[:times] ||= 0
    session[:times] += 1
    render text: "You visited this url #{session[:times]} times."
  end

  def times_restart
    session[:times] = nil
    render text: 'Destroyed the session!'
  end
end
