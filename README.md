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