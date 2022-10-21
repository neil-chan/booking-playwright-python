build:
	docker-compose down --rmi all && docker-compose build

test:
	docker-compose up && docker-compose down