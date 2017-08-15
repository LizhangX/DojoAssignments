class SecretsController < ApplicationController
  def index 
    @secrets = Secret.all
  end

  def create
    secret = Secret.new(secret_params)
    secret.user = User.find(params[:id])
    secret.save
    return redirect_to :back
  end

  def destroy
    # return redirect_to "users/#{current_user.id}" unless params[:id] == current_user.id
    Secret.find(params[:id]).destroy
    return redirect_to "/users/#{current_user.id}"
  end

  private
    def secret_params 
      params.require(:secret).permit(:content)
    end

end
