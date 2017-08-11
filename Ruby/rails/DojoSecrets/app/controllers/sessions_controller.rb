class SessionsController < ApplicationController
def new
    # render login page
end
def create
    # Log User In
    @user = User.find_by_email(params[:email]).try(:authenticate,params[:password])
    if @user
        session[:user_id] = @user.id
        return redirect_to "/users/#{@user.id}"
    else
        flash[:errors] = 'Invalid Combination'
        return redirect_to :back
    end
    # if authenticate true
        # save user id to session
        # redirect to users profile page
    # if authenticate false
        # add an error message -> flash[:errors] = ["Invalid"]
        # redirect to login page
end
def destroy
    session[:user_id] = nil
    return redirect_to '/sessions/new'
    # Log User out
    # set session[:user_id] to null
    # redirect to login page
end
end
