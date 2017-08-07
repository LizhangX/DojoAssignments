class RpgController < ApplicationController

  def index
    session[:gold] ||= 0
    session[:activities] ||= []
    @activities = session[:activities]
    render 'index'
  end

  def farm
    num = rand(10..20)
    puts "this is my #{num}"
    session[:gold] += num
    session[:activities] << "Earned #{num} golds from the farm! (#{Time.current.strftime('%Y/%m/%d %l:%M %P')})"
    redirect_to '/'
  end

  def cave
    num = rand(5..10)
    puts "this is my #{num}"
    session[:gold] += num
    session[:activities] << "Earned #{num} golds from the cave! (#{Time.current.strftime('%Y/%m/%d %l:%M %P')})"    
    redirect_to '/'
  end

  def house
    num = rand(2..5)
    puts "this is my #{num}"
    session[:gold] += num
    session[:activities] << "Earned #{num} golds from the house! (#{Time.current.strftime('%Y/%m/%d %l:%M %P')})"    
    redirect_to '/'
  end

  def casino
    num = rand(-50..50)
    puts "this is my #{num}"
    if session[:gold] == 0
        session[:activities] << "You cannot go to casino casuse you don't have any gold!!"
        return redirect_to '/'
    end
    if num < 0
      num = num * -1
      temp = session[:gold]
      session[:gold] -= num
      
      if session[:gold] < 0
        num = temp
        session[:gold] = 0
      end
      session[:activities] << "Entered a casino and lost #{num} golds... Ouch.. (#{Time.current.strftime('%Y/%m/%d %l:%M %P')})"  
    else
      session[:activities] << "Earned #{num} golds from the Casino! (#{Time.current})"
      session[:gold] += num
    end
    redirect_to '/'
  end

end
