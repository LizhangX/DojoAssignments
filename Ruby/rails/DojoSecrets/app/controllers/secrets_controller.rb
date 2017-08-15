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
    Secret.find(params[:id]).destroy
    return redirect_to "/users/#{params[:user_id]}"
  end

  private
    def secret_params 
      params.require(:secret).permit(:content)
    end

end
