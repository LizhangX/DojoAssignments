class LikesController < ApplicationController
  def create
    @like = Like.new()
    @like.user = User.find(params[:user_id])
    @like.secret = Secret.find(params[:id])
    @like.save
    return redirect_to :back
  end

  def destroy
    Like.find_by(user_id: params[:user_id]).destroy
    return redirect_to :back
  end
end
