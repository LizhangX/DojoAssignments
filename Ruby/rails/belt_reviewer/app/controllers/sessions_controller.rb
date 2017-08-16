class SessionsController < ApplicationController

    def create
        user = User.find_by_email(params[:email]).try(:authenticate, params[:password])
        if user
            session[:user_id] = user.id
            return redirect_to "/events"
        else
            flash[:errors] = ['Invalid Combination']
            return redirect_to :back
        end
    end

    def destroy
        session[:user_id] = nil
        return redirect_to '/'
    end

end
