from os import path
from unittest import TestCase

from config.database import setup_database, teardown_database
from tests.definitions import TESTS_DIR
from services.competency_repository import CompetencyRepository
from models import commit, db_session, db
from models import Competency
from models import struct

db_settings = {'provider': 'sqlite', 'filename': path.join(TESTS_DIR, 'test.sqlite'), 'create_db': True}
setup_database(db, db_settings, reset_database=True, sql_debug=True)


class TestCompetencyRepository(TestCase):
    @classmethod
    @db_session
    def setUpClass(self):
        parent = Competency(uuid='23df-44bc-aac2', description='Competency 1', category='Cat 1', children=[])
        Competency(uuid='23df-44bc-bbc2', description='Competency 2', category='Cat 1', children=[])
        Competency(uuid='23df-44bc-aac3', description='Sub Competency 1', category='Cat 1', children=[], parent=parent)
        commit()

    @classmethod
    def tearDownClass(cls):
        teardown_database(db)

    def test_find_all(self):
        expected_result = [
            struct.Competency(id=1, uuid='23df-44bc-aac2', description='Competency 1', category='Cat 1',
                              children=[
                                  struct.Competency(id=3, uuid='23df-44bc-aac3', description='Sub Competency 1',
                                                    category='Cat 1', children=[])
                              ]),
            struct.Competency(id=2, uuid='23df-44bc-bbc2', description='Competency 2', category='Cat 1', children=[])
        ]
        result = CompetencyRepository().find_all()
        assert result == expected_result
