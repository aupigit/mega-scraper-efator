deps:
	poetry install

test: deps
	poetry run pytest -vvv

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

rundb:
	if [hash docker-compose >/dev/null]; \
	then \
		sudo docker-compose -f docker-compose-devdb.yml up -d --build; \
	else \
		sudo docker compose -f docker-compose-devdb.yml up -d --build; \
	fi \

stopdb:
	if [hash docker-compose >/dev/null]; \
	then \
		sudo docker-compose -f  docker-compose-devdb.yml down; \
	else \
		sudo docker compose -f  docker-compose-devdb.yml down; \
	fi \

runserver:
	poetry run ./app/manage.py runserver 0.0.0.0:8000

createsuperuser:
	poetry run ./app/manage.py createsuperuser

migrate:
	poetry run ./app/manage.py migrate

makemigrations:
	poetry run ./app/manage.py makemigrations

makemigrations-merge:
	poetry run ./app/manage.py makemigrations --merge

