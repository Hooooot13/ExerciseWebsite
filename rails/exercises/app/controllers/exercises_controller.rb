class ExercisesController < ApplicationController
    def index
        @exercises = Exercise.all.sort_by &:name
    end
    def show
        @exercise = Exercise.find params[:id]
    end
    def update
        exercise = Exercise.find params[:id]
        exercise.update params.permit(:name)
    end
end
