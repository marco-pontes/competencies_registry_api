from models.entity import *


# publicationStatus: Deprecated
# publicationStatus: Draft
# publicationStatus: Published
class ConceptScheme(db.Entity):
    def __init__(self, uuid, name, description, publisher, creator, languages, publication_status, concepts, date_created, date_updated):
        self.uuid = uuid
        self.name = name
        self.description = description
        self.publisher = publisher
        self.creator = creator
        self.languages = languages
        self.publication_status = publication_status
        self.concepts = concepts
        self.date_created = date_created
        self.date_updated = date_updated