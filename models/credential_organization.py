from models.entity import *


#agentSector: PrivateForProfit
#agentSector: PrivateNonProfit
#agentSector: Public

# orgType: AssessmentBody
# orgType: Business
# orgType: BusinessAssociation
# orgType: CertificationBody
# orgType: Collaborative
# orgType: CoordinatingBody
# orgType: FourYear
# orgType: Government
# orgType: HighSchool
# orgType: LaborUnion
# orgType: Magnet
# orgType: Military
# orgType: NonTraditional
# orgType: Postsecondary
# orgType: PrimarilyOnline
# orgType: ProfessionalAssociation
# orgType: QualityAssurance
# orgType: SecondarySchool
# orgType: Technical
# orgType: TrainingProvider
# orgType: TwoYear
# orgType: Vendor
class CredentialOrganization(db.Entity):
    id = PrimaryKey(int, auto=True)
    uuid = Required(str, unique=True)
    name = Required(str)
    description = Required(str)
    webpage = Required(str)
    badges = Set('DigitalBadge')
    competency_frameworks = Set('CompetencyFramework')
    #address = Required(str)
    agent_type = Required(str)
    agent_sector = Required(str)