Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  root  "exercises#index"
  
  get   "/exercises/:id", to: "exercises#show"
  patch "/exercises/:id", to: "exercises#update"
end
