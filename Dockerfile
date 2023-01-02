FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
COPY task_manager/ /app/task_manager
COPY pyproject.toml /app
COPY README.md manage.py .env /app
COPY docker/services/task-manager/docker-entrypoint.sh /app

WORKDIR /app
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["./docker-entrypoint.sh"]
