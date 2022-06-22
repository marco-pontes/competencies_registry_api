nv# Competencies Registry Importer/API

This project is based on the Learning Tapestry developer [test challenge](https://github.com/learningtapestry/learning-tapestry-developer-test) and contains three main components:

- A registry API data fetcher and database populator(currently uses sqlite, postgres still being implemented).
- An API for a frontend application.
- The React frontend that consumes the API(WIP).

## Configuration

1. Clone the repo:

```bash
git clone https://github.com/marco-pontes/competencies_registry_api.git
```

3. Go to the project directory

```bash
cd competencies_registry_api
```

4. Install the project dependencies using python virtualenv to setup the environment for you:
```bash
python -m venv .env && source .env/bin/activate && pip install -r requirements.txt
```

5. Run the data importer to populate the database:

```bash
PYTHONPATH=$(pwd) python data_importer/main.py       
```

6. Start the API:

```bash
uvicorn api:app --reload
```


## Resources Importer

The resources importer creates a cache of all the needed resources present on the registry API. Those resources are analysed to create a dependency tree that is going to be imported to the database.

To run the resources importer, simply execute:
```bash
PYTHONPATH=$(pwd) python data_importer/main.py       
```
***Commited cache files for testing purposes. That way someone can test the program faster, without waiting for all the needed resources to download from the API. If you prefer, you can delete the .cache folder and wait for the importer to request all the necessary data.***


## API

The API uses FastAPI to make the resources saved to the database available to be used on a frontend application.
The API is served on [http://localhost:8000](http://127.0.0.1:8000)

Current API endpoints:
- /competencies

To start the API run:
```bash
uvicorn api:app --reload
```

Api docs: http://127.0.0.1:8000/docs

## React Frontend

WIP

## Testing

Python backend code can be tested using the following command:
```bash
python -m pytest tests 
```