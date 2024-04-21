start: # Starts the project in the background
	@docker compose up --build -d

stop: # Stops the project
	@docker compose stop

connect: # Connects to the container
	@docker exec -it jet_app bash

dependecies-update: # Updates the dependencies
	@docker exec -it jet_app poetry install

test: # Runs the tests
	@docker exec -it jet_app poetry run pytest