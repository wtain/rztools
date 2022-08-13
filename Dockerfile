# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY . .

WORKDIR /python-docker/FindDuplicateFiles
RUN pip3 install -r requirements.txt

WORKDIR /python-docker/ImageServer
RUN pip3 install -r requirements.txt

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-h", "duplicates_store"]
# , "-h", "duplicates_store"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# ENTRYPOINT [ "python3" ]
# CMD [ "app.py", "-h", "duplicates_store" ]
