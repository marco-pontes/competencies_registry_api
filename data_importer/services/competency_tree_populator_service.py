from data_importer.resources.resource_url import ResourceURL
from models import db_session, commit, Competency


class CompetencyTreePopulatorService:
    def __init__(self, json_resources_manager):
        self.json_resources_manager = json_resources_manager

    @db_session
    def run(self, uuids):
        for uuid in uuids:
            json_resource = self.json_resources_manager.load_resource_by_id(uuid)
            self.save_competency(json_resource)
        commit()

    def save_competency(self, competency_data):
        if "ceasn:isChildOf" in competency_data:
            parent_list = competency_data['ceasn:isChildOf']
            parent_url = parent_list[0]
            resource_url = ResourceURL(url=parent_url)
            parent_uuid = resource_url.uuid
            parent = self.json_resources_manager.load_resource_by_id(parent_uuid)
            self.save_competency(parent)
            Competency.from_json(competency_data)
        Competency.from_json(competency_data)


