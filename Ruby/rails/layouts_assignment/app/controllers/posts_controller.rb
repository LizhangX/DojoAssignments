class PostsController < ApplicationController
  
  layout "three_column", only: [:index]
  def index
    @posts = Post.all
    @users = User.all
  end

  def create
    Post.create(post_param)
    return redirect_to '/posts'
  end

  private
    def post_param
      params.require(:post).permit(:title, :content, :user_id)
    end
end
