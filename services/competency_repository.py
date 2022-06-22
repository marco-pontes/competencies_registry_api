from models import db_session, Competency, struct


class CompetencyRepository:
    @db_session
    def find_all(self):
        competency_records = Competency.select(parent=None)[:]
        competencies = self.convert_records_to_structs(competency_records)
        return competencies

    def convert_records_to_structs(self, competencies):
        competencies_structs = []
        for competency in competencies:
            children = self.convert_records_to_structs(competency.children)
            competency_struct = struct.Competency(competency.id, competency.uuid, competency.description, competency.category, children)
            competencies_structs.append(competency_struct)
        return competencies_structs

