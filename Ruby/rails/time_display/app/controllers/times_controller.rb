class TimesController < ApplicationController
  def main
    @timenow = DateTime.now.strftime('%c')
  end
end
