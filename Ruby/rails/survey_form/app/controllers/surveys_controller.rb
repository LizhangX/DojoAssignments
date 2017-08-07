class SurveysController < ApplicationController
  def index
    render 'index'
  end

  def create
    session[:survey] = params[:survey]
    session[:time] ||= 0
    session[:time] += 1
    flash[:success] = "Thanks for submmiting the form! You have submitted this form for #{session[:time]} times now!"
    redirect_to '/surveys/show'
  end

  def show
    render 'show'
  end
end
