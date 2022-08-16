# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

# COPY . .
# VOLUME .:/python-docker

# WORKDIR /python-docker/FindDuplicateFiles
# RUN pip3 install -r requirements.txt

COPY requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /python-docker/ImageServer
# RUN pip3 install -r requirements.txt

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-h", "duplicates_store"]
# , "-h", "duplicates_store"

# Enable debug mode for Flask
ENV FLASK_DEBUG 1

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# Debug container
# ENTRYPOINT ["tail", "-f", "/dev/null"]

# ENTRYPOINT [ "python3" ]
# CMD [ "app.py", "-h", "duplicates_store" ]


# For Ping
# RUN apt-get update && apt-get install -y iputils-ping
# to ping host.docker.internal