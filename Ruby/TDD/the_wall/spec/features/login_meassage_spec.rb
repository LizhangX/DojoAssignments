require 'rails_helper'
feature "login" do
    before(:each) do
        visit new_user_path
    end

    scenario "successfully creates a new user account if it does not exist" do
        fill_in "user_username", with: "Lizhang"
        click_button "Sign in"
        expect(page).to have_content "Welcome, Lizhang"
        expect(page).to have_current_path(messages_path)
    end

    scenario "successfully creates a new user account if it exist" do
        User.create(username: "Lizhang")
        fill_in "user_username", with: "Lizhang"
        click_button "Sign in"
        expect(page).to have_content "Welcome, Lizhang"
        expect(page).to have_current_path(messages_path)
    end

    scenario "unsuccessfully creates a new user" do
        click_button "Sign in"
        expect(current_path).to eq(new_user_path)
    end
    
    scenario "doesn't fill out username field" do
        click_button "Sign in"
        expect(page).to have_content "Username can't be blank"    
    end

    scenario "doesn't have at least 5 characters for username" do
        fill_in "user_username", with: "liz"
        click_button "Sign in"
        expect(page).to have_content "Username is too short (minimum is 5 characters)"
    end

end

feature "create message" do
    before(:each) do
        visit new_user_path
        fill_in "user_username", with: "Lizhang"
        click_button "Sign in"
    end

    scenario "successfully creates a message" do
        fill_in "message_message", with: "this is a message"
        click_button "Post a Message"
        expect(page).to have_current_path(messages_path)
        expect(page).to have_content "this is a message"
    end

    scenario "unsuccessfully creates a message" do
        click_button "Post a Message"
        expect(page).to have_current_path(messages_path)
    end

    scenario "doesn't fillout the message" do
        click_button "Post a Message"
        expect(page).to have_content "Message can't be blank"
    end

    scenario "doesn't have at least 10 characters for message" do
        fill_in "message_message", with: "message"
        click_button "Post a Message"
        expect(page).to have_content "Message is too short (minimum is 10 characters)"
    end

end

feature "logout" do
    before(:each) do
        visit new_user_path
        fill_in "user_username", with: "Lizhang"
        click_button "Sign in"
    end

    scenario "successfully logout" do
        click_link "Logout"
        expect(page).to have_current_path(new_user_path)
    end
end