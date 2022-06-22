import logging
from os import path

from data_importer.decoder.data_decoder import DataDecoder
from data_importer.json.api_client import ApiClient
from data_importer.json.cache_manager import CacheManager
from data_importer.resources.resources_manager import ResourcesManager
from data_importer.resources.tree_data_loader import TreeDataLoader

from data_importer.services.competency_tree_database_populator_service import CompetencyTreeDatabasePopulatorService
from definitions import ROOT_DIR
from models import db
from config.database import setup_database

db_settings = {'provider': 'sqlite', 'filename': path.join(ROOT_DIR, 'database.sqlite'), 'create_db': True}
setup_database(db, db_settings, reset_database=True, sql_debug=True)

logging.basicConfig(level=logging.INFO)

api_client = ApiClient()
cache_manager = CacheManager()
resources_manager = ResourcesManager(api_client, cache_manager)
tree_data_loader = TreeDataLoader(resources_manager)
data_decoder = DataDecoder()

api_records = resources_manager.load_all_resources()

for record in api_records:
    decoded_record = data_decoder.decode(record)
    tree_data_loader.load_related_resources_tree(decoded_record)


competencies_ids = tree_data_loader.loaded_resources_by_type['ceasn:Competency']
CompetencyTreeDatabasePopulatorService(resources_manager).run(competencies_ids)

#Missing classes to insert into the database
# CredentialOrganization
# DigitalBadge
# CompetencyFramework