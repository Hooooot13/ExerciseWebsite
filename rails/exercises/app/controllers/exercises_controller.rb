class ExercisesController < ApplicationController
    def index
        @exercises = Exercise.all
    end
    def show
        @exercise = Exercise.find_by name: params[:name]
    end
end
