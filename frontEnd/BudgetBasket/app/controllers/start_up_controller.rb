class StartUpController < ApplicationController
    def button
        system (Dir.pwd + '/scripts/autoPopulateActiveRecords.py')
        redirect_to '/'
    end
end
