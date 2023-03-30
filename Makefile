cnf ?= .env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))
up:
	sudo docker-compose --env-file ./.env up --build
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps
db:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE DATABASE ${POSTGRES_DB};"
init:
	sudo docker-compose --env-file ./.env exec web flask db init
migrate:
	sudo docker-compose --env-file ./.env exec web flask db migrate
drop:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "DROP DATABASE ${POSTGRES_DB};"
stop:
	sudo docker-compose down
clear:
	sudo docker volume rm $(docker volume ls -q)
	sudo docker system prune -a

