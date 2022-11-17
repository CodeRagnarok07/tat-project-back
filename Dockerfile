FROM python:3.8.15-alpine3.16

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update
RUN apk add gcc musl-dev python3-dev jpeg-dev zlib-dev
RUN apk add postgresql-dev

RUN pip install --upgrade pip
COPY ./requirements-docker.txt ./
RUN python -m pip install -r requirements-docker.txt


# RUN apk add mysql-client mariadb-dev mariadb-connector-c-dev
# RUN python -m pip install mysqlclient

COPY ./ ./

EXPOSE 8000

# RUN python manage.py migrate
# RUN python manage.py loaddata ./db/data.json
# Collect static files
# RUN python -m manage collectstatic -v 3 --no-input
CMD ["sh", "entrypoint.sh"]







