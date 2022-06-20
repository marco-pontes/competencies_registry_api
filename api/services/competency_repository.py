from models import db_session, Competency


class CompetencyRepository:
    @db_session
    def find_all(self):
        return Competency.select()


