from os import path

from fastapi import FastAPI

from definitions import ROOT_DIR
from models import db
from config.database import setup_database
from presenters import CompetencyPresenter

from services import CompetencyRepository
app = FastAPI()

db_settings = {'provider': 'sqlite', 'filename': path.join(ROOT_DIR, 'database.sqlite'), 'create_db': False}
setup_database(db, db_settings, reset_database=False, sql_debug=True)

@app.get("/competencies")
async def competencies():
    competency_repository = CompetencyRepository()
    competencies = competency_repository.find_all()
    return CompetencyPresenter.present(competencies)
