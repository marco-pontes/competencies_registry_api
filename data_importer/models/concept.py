from data_importer.models.entity import *

class Concept(db.Entity):
    def __init__(self, uuid, label, scheme_id):
        self.uuid = uuid
        self.scheme_id = scheme_id
        self.label = label