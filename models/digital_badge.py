from models.entity import *


# credentialStat: Active
# credentialStat: Deprecated
# credentialStat: Probationary
# credentialStat: Suspended
class DigitalBadge(db.Entity):
    id = PrimaryKey(int, auto=True)
    uuid = Required(str, unique=True)
    name = Required(str)
    description = Required(str)
    language = Required(str)
    webpage = Required(str)
    credential_status = Required(str)
    credential_organization = Required('CredentialOrganization')