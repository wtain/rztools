
### Install Docker

To run MongoDB from Docker, Docker Desktop to be installed. 
On Windows it is also required to enable WSL to use Docker.

### Install MongoSh

In order to work with MondoDB, download MongoSh: 
https://www.mongodb.com/try/download/shell

It would also be convenient to add appropriate environment variables and update PATH environment variable to use mongosh from anywhere

## Usage

### Create network

```bash
docker network create image_network
```

### Create Volume

(Not used now)
```bash
docker volume create mongodbdata
```

### Run MongoDB

```bash
docker run -p 27017:27017 -v %cd%/data/db:/data/db --net image_network -d --name=duplicates_store mongo:latest --noauth --bind_ip=0.0.0.0
```


