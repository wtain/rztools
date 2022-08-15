# RZTools

### Install

#### rename_pdf_bulk

```bash
pip3 install PyPDF2
```

#### FindDuplicateFiles

```bash
```


## Build Docker image

```bash
docker build --tag python-docker .
```

## Run

```bash
docker run -d -p 5000:5000 --net image_network python-docker
```

## Run with Docker-Compose
```bash
docker-compose up
```

```bash
# Build images before starting containers.
docker-compose up --build
# Recreate containers even if configuration/image hasn't changed.
docker-compose up --force-recreate

docker-compose up -d --no-deps --build <service_name>

docker build .

docker-compose up --build
docker-compose up
docker-compose down
```