from models.entity import *


# publicationStatus: Deprecated
# publicationStatus: Draft
# publicationStatus: Published
class CompetencyFramework(db.Entity):
    id = PrimaryKey(int, auto=True)
    uuid = Required(str, unique=True)
    name = Required(str)
    source = Required(StrArray)
    license = Required(str)
    publisher = Required('CredentialOrganization')
    description = Required(str)
    publication_status = Required(str)
    competencies = Set('Competency')