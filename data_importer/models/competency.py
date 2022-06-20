from data_importer.models.entity import *

from data_importer.resources.resource_url import ResourceURL


class Competency(db.Entity):
    id = PrimaryKey(int, auto=True)
    uuid = Required(str, unique=True)
    description = Optional(str)
    category = Optional(str)
    parent = Optional("Competency")
    children = Set("Competency")
    framework = Optional("CompetencyFramework")

    def from_json(json_data):
        uuid = json_data['ceterms:ctid']
        competency = Competency.get(uuid=uuid)
        parent_competency = None
        if competency is None:
            description = json_data.get('ceasn:competencyText', {}).get('en-us', '')
            category = json_data.get('ceasn:competencyCategory', {}).get('en-us', '')
            if "ceasn:isChildOf" in json_data:
                parent_list = json_data['ceasn:isChildOf']
                parent_url = parent_list[0]
                resource_url = ResourceURL(parent_url)
                parent_uuid = resource_url.uuid
                parent_competency = Competency.get(uuid=parent_uuid)
            competency = Competency(uuid=uuid, description=description, category=category, parent=parent_competency)
        return competency


Competency.from_json = staticmethod(Competency.from_json)