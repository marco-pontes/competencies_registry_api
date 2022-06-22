class CompetencyPresenter:
    def present(competencies):
        competencies_as_json = CompetencyPresenter.convert_to_json(competencies)
        return competencies_as_json

    def convert_to_json(competencies):
        competencies_as_json = []
        for competency in competencies:
            children = CompetencyPresenter.convert_to_json(competency.children)
            json = {'label': competency.description, 'value': competency.id, 'children': children}
            competencies_as_json.append(json)
        return competencies_as_json


CompetencyPresenter.present = staticmethod(CompetencyPresenter.present)
CompetencyPresenter.convert_to_json = staticmethod(CompetencyPresenter.convert_to_json)
