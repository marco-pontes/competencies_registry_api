from os import path

from pony.orm import set_sql_debug

def setup_database(db, settings, reset_database=False, sql_debug=False):
    set_sql_debug(sql_debug)
    if db.provider is None:
        db.bind(settings)
    if db.schema is None:
        db.generate_mapping(create_tables=True)
    if reset_database:
        db.drop_all_tables(with_all_data=True)
        db.create_tables()


def teardown_database(db):
    if db.schema:
        db.drop_all_tables(with_all_data=True)
    db.disconnect()
