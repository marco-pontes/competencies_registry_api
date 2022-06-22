from presenters import CompetencyPresenter
from models.struct import Competency


class TestCompetencyPresenter:
    def test_present(self):
        expected_result = [{'label': 'Competency 1', 'value': 1, 'children': [{'label': 'Sub Competency 1', 'value': 2, 'children':[]}]}, {'label': 'Competency 2', 'value': 3, 'children': []}]
        competencies = [Competency(id=1, uuid='23df-44bc-aac2', description='Competency 1', category='Cat 1', children=[
            Competency(id=2, uuid='23df-44bc-aac3', description='Sub Competency 1', category='Cat 1', children=[])
        ]), Competency(id=3, uuid='23df-44bc-bbc2', description='Competency 2', category='Cat 1', children=[])]
        result = CompetencyPresenter.present(competencies)
        assert result == expected_result


