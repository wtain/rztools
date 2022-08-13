
# FindDuplicateFiles

## Description

This tool traverses filesystem and gathers file hashes. Then groups files by their hashes and reports statistics. 
This is useful to find duplicate files and decide which to remove in order to save disk space.

## Install

### Install PyMongo

```bash
pip install pymongo
pip install Pillow
``` 

Run ``main.py`` with command line arguments from the root folder of rztools:

### Run the script

```bash
python main.py -d "j:\My Drive\Pictures" -b 131072
```

d - is path for the files to check
b - block size for hash calculation. Default is 65536. SHA256 is currently used.

### Checking results in MongoSh

First run this statement to select teh database
```
use duplicates_store
```

Show all files
```
db.files.find()
```

Find all files by hash
```
db.files.find({ hash: "8cddf9ddc5ce4fd09dbc4ba4f0f8c262bec4a7e65782f4b35605906e3e87f2de"})
```

Delete all
```
db.files.remove({})
```


### Dump requirements
```bash
pip3 freeze > requirements.txt
```