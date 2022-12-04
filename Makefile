MANAGE := poetry run python3 manage.py

start:
	${MANAGE} runserver 127.0.0.1:8000
shell:
	${MANAGE} shell_plus --plain
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate
test:
	${MANAGE} test
#translate:
#	${MANAGE} makemessages -l ru --no-default-ignore --ignore=*venv*
#	${MANAGE} compilemessages

lint:
	poetry run flake8 task_manager
