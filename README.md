# Competencies Registry Importer/API


## Configuration

1. Clone the repo:

```bash
git clone https://github.com/marco-pontes/competencies_registry_api.git
```

3. Go to the project directory

```bash
cd competencies_registry_api
```

4. Install the project dependencies

```bash
pip install requests 

pip install pyjwt 

pip install validators

pip install pony 

pip install -U pytest
```

or use python virtualenv to setup the environment for you:
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

## Resources Importer

The resources importer creates a cache of all the needed resources present on the registry API. Those resources are analysed to create a dependency tree that is going to be imported to the database.

To run the resources importer, simply execute:
```bash
PYTHONPATH=$(pwd) python data_importer/main.py       
```
***Commited cache files for testing purposes. That way someone can test the program faster, without waiting for all the needed resources to download from the API. If you prefer, you can delete the .cache folder and wait for the importer to request all the necessary data.***


## API

The API will make the resources saved to the database available as an API to be used on a frontend application. This is still a work in progress.

## Testing

```bash
python -m pytest . 
```