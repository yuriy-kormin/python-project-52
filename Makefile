MANAGE := poetry run python manage.py

start:
	${MANAGE} runserver 127.0.0.1:8000
shell:
	${MANAGE} shell_plus --plain
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate
lint:
	poetry run flake8 task_manager
