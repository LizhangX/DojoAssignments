require 'test_helper'

class DisplaysControllerTest < ActionController::TestCase
  test "should get index" do
    get :index
    assert_response :success
  end

  test "should get hello" do
    get :hello
    assert_response :success
  end

  test "should get say_hello" do
    get :say_hello
    assert_response :success
  end

  test "should get times" do
    get :times
    assert_response :success
  end

  test "should get times_restart" do
    get :times_restart
    assert_response :success
  end

end
