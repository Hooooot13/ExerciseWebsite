class ExercisesController < ApplicationController
    def index
        @exercises = Exercise.all.sort_by &:name
    end
    def show
        @exercise = Exercise.find_by name: params[:name]
    end
end
